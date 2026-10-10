# ADR-002: Recovery objectives

- **Status:** Proposed
- **Decision:** For a noncritical demo, target RPO <= 24 hours and RTO <= 8 hours, subject to data-tier backup features being configured and tested.
- **Definitions:** RPO = maximum acceptable data loss measured in time; RTO = target time to restore service.
- **Reason:** Simple, low-cost starting point for a learning service.
- **Trade-offs:** These objectives are not guaranteed by this repository alone. Configure storage soft delete/versioning, retention, and a documented restore test.
- **Validation:** Run a restore exercise and record the actual recovery time.
