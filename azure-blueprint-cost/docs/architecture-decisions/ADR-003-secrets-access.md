# ADR-003: Secrets and least privilege

- **Status:** Proposed
- **Decision:** Use Azure managed identity for application-to-storage access. Store deployment credentials only in GitHub Actions secrets or use federated identity/OIDC when configured. Never commit secrets.
- **Access:** Grant the app identity only the required Blob Storage data role at the narrowest practical scope. Keep developer and deployment permissions separate.
- **Reason:** Reduce credential leakage and limit the impact of a compromised identity.
- **Trade-offs:** Identity and role assignments must be configured in Azure; the starter template does not automatically grant data-plane permissions.
- **Validation:** Confirm access works without account keys and review role assignments.
