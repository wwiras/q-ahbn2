#!/usr/bin/env python3
"""Independent, read-only D8-A reconstruction; stdlib only, no cluster/network calls.

Outputs must be outside evidence. Exact JSON record deduplication follows the
committed logging contract; this is not message/peer deduplication.
"""
import argparse
import collections
import csv
import datetime
import hashlib
import json
import math
from pathlib import Path
import subprocess
from audit_d8_i1_sha256 import FORMAL_ROOT_SEEDS, METHODS, EXPECTED_RUN_FILES

REPO = Path(__file__).resolve().parents[2]
SOURCE = '6433f7429e0342df44c272b236423c65203a9136'
DIGEST = 'sha256:7e5a3d385e9dcd5c051505ef1fdcccab581539780db3e228cd1575dde1c1488f'
PRIMARY = ('delivery_ratio', 'propagation_delay', 'duplicates', 'total_forwards')
LABELS = dict(zip(METHODS, ('Gossip','Structured','DC-SoC','AHBN','Q-AHBN2')))

def canonical(x):
    return json.dumps(x, sort_keys=True, separators=(',', ':'))

def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024*1024), b''):
            h.update(block)
    return h.hexdigest()

def records(path):
    seen = set(); rows = []; repeated = 0; ignored = 0
    decoder = json.JSONDecoder()
    for no, line in enumerate(path.read_text().splitlines(), 1):
        pending = line.strip()
        if not pending.startswith('{'):
            ignored += bool(pending); continue
        while pending:
            try:
                row, end = decoder.raw_decode(pending)
            except ValueError as e:
                raise ValueError(f'{path}:{no}: malformed JSON') from e
            key = canonical(row)
            if key in seen: repeated += 1
            else: rows.append(row); seen.add(key)
            pending = pending[end:].lstrip()
    return rows, repeated, ignored

def reconstruct(rows, topo):
    by = collections.defaultdict(list)
    for r in rows: by[r.get('event')].append(r)
    arrivals = collections.defaultdict(list)
    for r in by['received_new']: arrivals[r['message_id']].append(r)
    state = sorted([(float(r['ts']), int(r['target_peer']), False) for r in by['pod_unavailability_observed']] +
                   [(float(r['ts']), int(r['target_peer']), True) for r in by['churn_rejoined']])
    opportunities = []; delays = []
    for inj in by['message_injected']:
        ts = float(inj['ts']); active = set(range(topo['num_nodes']))
        for at, peer, up in state:
            if at > ts: break
            if up: active.add(peer)
            else: active.discard(peer)
        rec = arrivals[inj['message_id']]; got = {int(r['peer_id']) for r in rec}
        times = [float(r['ts']) for r in rec if int(r['peer_id']) in active]
        opportunities.append(dict(message_id=inj['message_id'], injected_ts=ts,
            expected_count=len(active), delivered_count=len(active & got),
            full_delivery=active <= got, completion_ts=max(times) if active <= got and times else None))
        if rec: delays.append(max(float(r['ts']) for r in rec)-ts)
    expected = sum(o['expected_count'] for o in opportunities)
    recovered = []
    for join in sorted(by['churn_rejoined'], key=lambda r:r['event_index']):
        first = next((o for o in opportunities if o['injected_ts'] >= join['ts'] and o['full_delivery']), None)
        recovered.append(dict(event_index=join['event_index'], recovered=first is not None,
            recovery_time_s=first['completion_ts']-join['ts'] if first else None,
            recovery_message_id=first['message_id'] if first else None,
            censored=first is None, censored_at_s=topo['settle_time'] if first is None else None))
    return dict(delivery_ratio=sum(o['delivered_count'] for o in opportunities)/expected,
        propagation_delay=sum(delays)/len(delays) if delays else None,
        duplicates=len(by['received_duplicate']), total_forwards=len(by['forward']),
        F_success=len(by['forward']), F_attempt=len(by['k7_forward_attempt']),
        recovery_events=recovered), opportunities, by

def git(*args):
    return subprocess.check_output(['git', '-C', str(REPO), *args], text=True).strip()

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--evidence-dir', type=Path, default=REPO/'output/evidence')
    p.add_argument('--output-dir', type=Path, required=True)
    a = p.parse_args(); evidence = a.evidence_dir.resolve(); out = a.output_dir.resolve()
    if out == evidence or evidence in out.parents: p.error('output must be outside evidence')
    out.mkdir(parents=True, exist_ok=True)
    issues=[]; audit=[]; inventory=[]; timing=[]; comparisons=[]; pairing={}
    def issue(seed, method, path, kind, expected, observed, impact, status='OPEN'):
        issues.append(dict(id=f'D8A-{len(issues)+1:03}', seed=seed, method=method,
            evidence_path=str(path), type=kind, expected=expected, observed=observed,
            scientific_impact=impact, supporting_evidence=str(path), resolution_status=status))
    for rootname, seed in FORMAL_ROOT_SEEDS.items():
        root=evidence/rootname
        for path in sorted(root.rglob('*')):
            if path.is_file():
                rel=path.relative_to(evidence).as_posix()
                category='metadata' if path.name=='.DS_Store' else ('primary' if 'runs' in path.relative_to(root).parts else 'supporting')
                try: inventory.append(dict(path=rel,category=category,size=path.stat().st_size,sha256=sha(path),error=''))
                except OSError as e: inventory.append(dict(path=rel,category=category,size=None,sha256=None,error=str(e)))
        commit=(root/'git_commit.txt').read_text().strip(); digest=(root/'expected_image_digest.txt').read_text().strip()
        for method in METHODS:
            run=root/'runs'/f'seed{seed}'/method; relative=run.relative_to(evidence).as_posix()
            start=len(issues)
            def check(name, expected, observed, file='run_manifest.json', kind='inconsistent evidence'):
                if expected != observed:
                    issue(seed,method,f'{relative}/{file}',kind,{name:expected},{name:observed},'Requires reconciliation before interpretation')
            try:
                for name in EXPECTED_RUN_FILES:
                    if not (run/name).is_file(): issue(seed,method,f'{relative}/{name}','missing evidence','present','missing','Mandatory artifact unavailable')
                manifest=json.loads((run/'run_manifest.json').read_text()); metrics=json.loads((run/'metrics.json').read_text()); topo=json.loads((run/'topology.json').read_text())
                rows, repeated, ignored=records(run/'logs.jsonl'); rebuilt, opportunities, by=reconstruct(rows,topo)
                check('source_commit',SOURCE,commit,'../../git_commit.txt'); check('expected_image',DIGEST,digest,'../../expected_image_digest.txt')
                for obj, file in [(manifest,'run_manifest.json'),(metrics,'metrics.json')]:
                    check('seed',seed,obj.get('seed'),file); check('algorithm',method,obj.get('algorithm'),file)
                for key,value in dict(message_count=240,message_interval=0.4,frozen_targets=[0,5,10,15],churn_offsets=[1.,26.,51.,76.]).items(): check(key,value,manifest.get(key))
                for key,value in dict(num_nodes=20,topology_type='ba',ba_m=2,seed=seed,strategy=('cluster' if method=='structured' else method)).items(): check(key,value,topo.get(key),'topology.json')
                check('topology_workload',{'message_count':240,'message_interval':0.4},topo['workload'],'topology.json')
                check('S5','S5',topo['k5_h2']['actuator_treatment'],'topology.json')
                check('maintenance_isolation',method=='dcsoc',topo['dcsoc']['dynamic_maintenance'],'topology.json')
                check('run_id',f'k7_exp11_{method}_seed{seed}',metrics.get('run_id'),'metrics.json')
                check('source_avoids_targets',True,topo['message_source'] not in manifest['frozen_targets'],'topology.json')
                target=json.loads((root/'target-selection'/f'seed{seed}.json').read_text())
                check('target_selection_hash',target['selection_hash'],manifest['target_selection_hash'])
                check('selection_hash_recomputed',target['selection_hash'],hashlib.sha256(canonical({k:v for k,v in target.items() if k!='selection_hash'}).encode()).hexdigest(),'../../target-selection/seed'+str(seed)+'.json')
                check('generated_topology',json.loads((root/'generated'/f'{method}_seed{seed}.json').read_text()),topo,'topology.json')
                check('generated_config_sha256',sha(root/'configs'/f'{method}_seed{seed}.yaml'),sha(run/'generated_config.yaml'),'generated_config.yaml')
                check('contract_version','k7-exp11-v2',manifest['contract_version'])
                check('topology_algorithm',method,topo['k7_exp11']['algorithm'],'topology.json')
                check('topology_schedule_targets',[0,5,10,15],[r['target_peer'] for r in topo['k7_exp11']['planned_churn_schedule']],'topology.json')
                pair=dict(edges={k:v['neighbors'] for k,v in topo['nodes'].items()},source=topo['message_source'],targets=manifest['target_selection_hash'])
                if seed in pairing: check('within_seed_topology_source_targets',pairing[seed],pair,'topology.json')
                else: pairing[seed]=pair
                for key in (*PRIMARY,'F_attempt','F_success','recovery_events'):
                    check(key,metrics[key],rebuilt[key],'logs.jsonl')
                churn=json.loads((run/'churn_events.json').read_text())
                check('opportunity_counts',[(o['message_id'],o['expected_count'],o['delivered_count']) for o in churn['delivery_opportunities']],[(o['message_id'],o['expected_count'],o['delivered_count']) for o in opportunities],'churn_events.json')
                check('injections',240,len(by['message_injected']),'logs.jsonl'); check('controller_injections',240,len(by['k7_message_injection']),'logs.jsonl')
                epoch=manifest['experiment_epoch']; grid=max(abs(r['planned_injection_ts']-(epoch+(int(r['msg_id'][1:])-1)*0.4)) for r in by['k7_message_injection'])
                check('planned_grid_within_1us',True,grid<=1e-6,'controller.log')
                controller,_,_=records(run/'controller.log'); stream,_,_=records(run/'peer_stream.jsonl')
                check('controller_records_in_merged_log',True,{canonical(r) for r in controller}<={canonical(r) for r in rows},'controller.log')
                snapshot,_,_=records(run/'final_snapshot.jsonl')
                check('merged_record_union', {canonical(r) for r in controller+stream+snapshot}, {canonical(r) for r in rows}, 'logs.jsonl')
                check('stream_records_in_merged_log',True,{canonical(r) for r in stream}<={canonical(r) for r in rows},'peer_stream.jsonl')
                statuses={n:(run/n).read_text().strip() for n in ['experiment_exit_status.txt','cleanup_exit_status.txt','namespace_cleanup_exit_status.txt','helm_cleanup_exit_status.txt','cleanup_status.txt','namespace_check_error.txt','namespace_cleanup.txt']}
                for n in ['experiment_exit_status.txt','cleanup_exit_status.txt','namespace_cleanup_exit_status.txt','helm_cleanup_exit_status.txt']: check(n,'0',statuses[n],n)
                check('cleanup','PASS',statuses['cleanup_status.txt'],'cleanup_status.txt')
                pods=json.loads((run/'pods.json').read_text())['items']; ids=[]; ready=[]
                for pod in pods:
                    for c in pod.get('status',{}).get('containerStatuses',[]): ids.append(c.get('imageID'));ready.append(c.get('ready'))
                check('pod_count',20,len(pods),'pods.json'); check('ready',True,len(ready)==20 and all(ready),'pods.json')
                check('runtime_digest',True,bool(ids) and all(x and x.endswith(DIGEST) for x in ids),'pods.json')
                check('controller_status', ['Succeeded'],[x['status']['phase'] for x in json.loads((run/'controller_pods.json').read_text())['items']],'controller_pods.json')
                check('recorded_validator_pass_count',5,(root/'terminal.log').read_text().count('K7 RESULT VALIDATION PASS'),'../../terminal.log')
                check('join_count',4,len(by['churn_rejoined']),'controller.log')
                check('leave_count',4,len(by['churn_leave_scheduled']),'controller.log')
                check('namespace_error_empty','',statuses['namespace_check_error.txt'],'namespace_check_error.txt')
                check('namespace_deletion_recorded',True,'deleted' in statuses['namespace_cleanup.txt'],'namespace_cleanup.txt')
                for join in by['churn_rejoined']:
                    index=join['event_index']
                    check(f'churn_{index}_ordering',True,join['unavailable_time']<=join['recovery_ready_time']<=join['grpc_alive_time']<=join['ts'],'controller.log')
                    infra=next(x for x in metrics['recovery_metrics'] if x['event_id']==index)
                    check(f'T_infra_{index}',infra['T_infra'],join['grpc_alive_time']-join['unavailable_time'],'metrics.json')
                    check(f'T_ready_{index}',infra['T_ready'],join['recovery_ready_time']-join['unavailable_time'],'metrics.json')
                    post=[r for r in by['k7_forward_attempt'] if r['ts']>=join['ts'] and (r.get('sender')==join['target_peer'] or r.get('destination_peer')==join['target_peer'])]
                    availability=[r for r in by['peer_availability'] if r['ts']>=join['ts'] and r.get('target')==join['target_peer']]
                    timing.append(dict(seed=seed,method=method,kind='post_rejoin_observation_summary',record=dict(event_index=index,join_ts=join['ts'],attempts_involving_target=len(post),first_attempt_ts=min((r['ts'] for r in post),default=None),availability_records=len(availability),first_availability_ts=min((r['ts'] for r in availability),default=None),source_file=relative+'/logs.jsonl')))
                    timing.append(dict(seed=seed,method=method,kind='churn_rejoined',record=join))
                for event in ['k7_message_injection','churn_leave_scheduled','pod_unavailability_observed','p3g_rejoin_notification']:
                    for r in by[event]: timing.append(dict(seed=seed,method=method,kind=event,record=r))
                for r in metrics['recovery_events']: timing.append(dict(seed=seed,method=method,kind='recovery_result',record=r))
                reportfile = 'D7_F_SEED42_EVIDENCE_AUDIT_20261020.md' if seed==42 else (f'D7_F_SEED{seed}_EXECUTION_20261020.md' if seed<46 else 'D8_A_B_PRELIMINARY_RECONCILIATION_20261020.md')
                report=REPO/'docs/stages'/reportfile
                line=next(l for l in report.read_text().splitlines() if l.startswith('| '+LABELS[method]+' |'))
                cells=[c.strip() for c in line.split('|')[2:6]]
                for key,text in zip(PRIMARY,cells):
                    value=float(text); actual=metrics[key]; delta=actual-value
                    comparisons.append(dict(seed=seed,method=method,metric=key,report=reportfile,reported=text,archived=actual,delta=delta))
                    tolerance=0.5*10**(-len(text.split('.')[1])) if '.' in text else 0
                    if abs(delta)>tolerance+1e-15: issue(seed,method,str(report),'inconsistent evidence',text,actual,'Preliminary value differs beyond displayed precision')
                content_status='PASS' if len(issues)==start else 'REVIEW'
                issue(seed,method,relative+'/metrics.json','measurement ambiguity','Explicit recovery observation horizon and consistent censoring semantics',metrics['recovery_events'],'Reconstruction matches code; 18 s labels do not bound the post-rejoin search. D8-B must resolve interpretation.')
                audit.append(dict(seed=seed,method=method,run_id=metrics['run_id'],evidence_path=relative,**{k:metrics[k] for k in PRIMARY},F_attempt=metrics['F_attempt'],source_commit=commit,expected_image_digest=digest,runtime_image_ids=sorted(set(ids)),source_peer=topo['message_source'],target_selection_hash=manifest['target_selection_hash'],exact_duplicate_log_records=repeated,ignored_log_lines=ignored,expected_deliveries=sum(o['expected_count'] for o in opportunities),observed_deliveries=sum(o['delivered_count'] for o in opportunities),recovery_events=metrics['recovery_events'],statuses=statuses,max_grid_error_s=grid,max_injection_lateness_ms=max(r['injection_lateness_ms'] for r in by['k7_message_injection']),content_checks=content_status,scientific_status='PARTIAL: timing/measurement interpretation open'))
            except (OSError, ValueError, KeyError, StopIteration, ZeroDivisionError) as e:
                issue(seed,method,relative,'missing evidence','parseable complete run',str(e),'Run reconstruction incomplete')
                audit.append(dict(seed=seed,method=method,evidence_path=relative,content_checks='INCOMPLETE'))
    issue('ALL','ALL','inventory.json','administrative limitation','Trusted execution-time per-file SHA256 baseline','Unavailable for all 920 research files','Current-state fingerprints cannot establish unchanged-since-execution integrity','DOCUMENTED LIMITATION')
    issue('ALL','ALL','origin/main','administrative limitation','Live GitHub comparison','Offline committed snapshot ca4415b; no remote refresh','Remote freshness and full Drive-to-local byte parity remain unverified','OPEN')
    summary=dict(timestamp_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),audit_base_commit=git('rev-parse','HEAD'),source_commit=SOURCE,script_sha256=sha(Path(__file__)),evidence_root=str(evidence),runs=len(audit),content_pass=sum(r['content_checks']=='PASS' for r in audit),inventory=dict(collections.Counter(r['category'] for r in inventory)),read_errors=sum(bool(r['error']) for r in inventory),issues=len(issues),historical_integrity='No trusted execution-time per-file baseline; current hashes do not prove immutability',github_comparison='Local committed origin/main snapshot; no network access in offline task',stash_commit=git('rev-parse','stash@{0}'),decision='PARTIAL')
    for name,obj in [('audit.json',audit),('discrepancies.json',issues),('inventory.json',inventory),('preliminary_comparison.json',comparisons),('provenance.json',summary)]: (out/name).write_text(json.dumps(obj,indent=2)+'\n')
    with (out/'timing_observations.jsonl').open('w') as f:
        for row in timing: f.write(json.dumps(row)+'\n')
    keys=sorted(set().union(*(r.keys() for r in audit)))
    with (out/'audit.csv').open('w') as f:
        writer=csv.DictWriter(f,fieldnames=keys);writer.writeheader()
        for r in audit: writer.writerow({k:canonical(v) if isinstance(v,(list,dict)) else v for k,v in r.items()})
    print(json.dumps(summary,indent=2))

if __name__=='__main__': main()
