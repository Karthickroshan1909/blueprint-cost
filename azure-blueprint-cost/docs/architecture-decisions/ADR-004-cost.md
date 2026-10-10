# ADR-004: Cost envelope and scaling

- **Status:** Proposed
- **Decision:** Estimate low, medium, and high traffic separately. Start with the smallest appropriate App Service tier, set a budget alert, and scale only when measurements justify it.
- **Reason:** Avoid selecting infrastructure based only on peak assumptions.
- **Trade-offs:** Very low-cost tiers may have limits and may not meet production availability goals.
- **Validation:** Replace workbook placeholders with region-specific prices from the Azure Pricing Calculator and review actual Cost Management data monthly.
