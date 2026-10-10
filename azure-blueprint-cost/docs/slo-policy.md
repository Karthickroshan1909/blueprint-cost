# SLO Policy

These are proposed targets for a learning/demo service. Validate them against real measurements before treating them as commitments.

## Service Level Indicators (SLIs)
- **Availability SLI:** successful eligible requests / total eligible requests, excluding planned maintenance only if explicitly defined.
- **Latency SLI:** percentage of eligible requests completed in 500 ms or less, measured at the application boundary.
- **Dependency SLI:** successful data-tier operations / total data-tier operations.
- **Freshness/backup SLI:** latest successful backup or recovery point age, if durable data is introduced.

## Targets and error budget
- Monthly availability SLO: **99.5%**.
- Monthly latency SLO: **95% of requests <= 500 ms**.
- Monthly dependency success target: **99.5%**.
- For a 30-day month, a 99.5% availability SLO allows about **216 minutes** of unavailability (0.5% × 43,200 minutes).
- Error budget is the permitted failure portion of the SLO period. If consumed quickly, pause risky releases and prioritize reliability work.

## Paging and ticket thresholds
- **Page:** availability below 99% over a 5-minute window, or sustained 5xx rate above 5% for 5 minutes.
- **Page:** p95 latency above 1 second for 10 minutes when traffic is sufficient to be meaningful.
- **Ticket / investigate:** dependency failure above 1% for 15 minutes.
- **Ticket / investigate:** monthly error budget consumption reaches 50%; review at 75%; freeze risky changes at 100%.
- Avoid paging on a single failed request. Use sustained windows and actionable alerts.

## Measurement notes
- Use Application Insights request and dependency telemetry.
- Record deployment version and correlation IDs in logs.
- Review SLOs monthly; adjust targets based on observed user needs and cost.
- A target is not proof of achieved performance: attach measured dashboard screenshots after deployment.
