# K3-Q inherited GKE provenance

Pinned source runtime: `wwiras/ahbn2_gke@cc7ce17ca489ed4a0eaf8c7bb2ebfa0c9780b689`.

Inherited files under `gke/app/` and `gke/helm/ahbn/` are deployment/runtime dependencies copied without scientific redesign. Q-AHBN2-specific additions are limited to `gke/app/qahbn2_runtime.py`, the frozen `qahbn2/` learner/transition modules, the Q-AHBN2 Docker recipe, and K3-Q smoke assets.

The four inherited strategies remain scientific baselines and are not reimplemented.
