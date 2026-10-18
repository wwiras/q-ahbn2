# P3G-REG-PUBLISH — researcher authorization and execution boundary (2026-10-18)

**Approval:** The researcher explicitly authorized exactly one candidate image publication to `docker.io/wwiras/q-ahbn2`. Approval does **not** extend to any GKE deployment, canary, D7-F, or D8.

**Preconditions:** exact approved source sha; clean checkout; private Docker Hub credentials; OCI revision label and all recovery-related modules; single unique nonmoving tag; validated registry manifest digest; source SHA and SHA256 evidence. Do not overwrite historical tag or use a local image ID as a registry digest.

**Connection blocker:** The linked GitHub connector offers repository writes and read-only workflow result inspection but no authorized GitHub Actions workflow-dispatch endpoint or Docker Hub registry push operation. An attempt to stage the publishing workflow was rejected by a tool safety check, so no release workflow was installed and no registry image was published. Do not claim publication or immutable digest.

**Next operation after the action is technically enabled:** publish the *one* approved candidate through a supported credentialed workflow; verify registry read-back digest and archive the receipt. Keep canary release separate.

**Status:** IMAGE REGISTRY PUSH NOT EXECUTED / BLOCKED BY ACTION ACCESS. Last independently verified offline image build: https://github.com/wwiras/q-ahbn2/actions/runs/39127329941. D7-F and D8 HOLD. Journal of Cloud Computing manuscript under peer review, no DOI.
