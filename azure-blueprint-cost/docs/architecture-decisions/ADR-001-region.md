# ADR-001: Azure region

- **Status:** Proposed
- **Decision:** Start in an Azure region close to the expected users and supported by all required services; for an India-focused demo, compare Central India and South India availability and pricing before selecting.
- **Reason:** Lower network latency and simpler operational ownership.
- **Trade-offs:** Region availability, quotas, service SKU support, and prices differ. A single-region design does not provide regional disaster recovery.
- **Validation:** Confirm service availability and final price in Azure portal and Azure Pricing Calculator.
