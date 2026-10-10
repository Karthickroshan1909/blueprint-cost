# Azure Service Blueprint, SLOs & Cloud Cost Envelope

A beginner-friendly cloud operations planning project for a small two-tier web service on Microsoft Azure.

## Project goal
Define the service's operational contract **before** selecting production infrastructure:
- request, dependency, deployment, data, and failure paths
- availability and latency SLIs/SLOs, error budget, and paging thresholds
- monthly cost estimates for low, medium, and high traffic
- architecture decisions for region, recovery, secrets, and least privilege

## Proposed demo architecture
- **Web/API tier:** Python Flask app, designed for Azure App Service
- **Data tier:** Azure Blob Storage for a small demo's persistent object/data records
- **Monitoring:** Azure Monitor / Application Insights (planned)
- **Delivery:** GitHub Actions workflow (deployment requires your Azure app and GitHub secrets)

> Cost figures in `cost-model.xlsx` are planning placeholders, not live Azure quotes. Replace them using the [Azure Pricing Calculator](https://azure.microsoft.com/pricing/calculator/) for your selected region and service tiers.

## Repository contents
- `docs/service-blueprint.md` — architecture and operational paths
- `docs/slo-policy.md` — SLIs, SLOs, error budget, alerting
- `docs/architecture-decisions/` — ADRs
- `workbooks/slo-workbook.xlsx` — editable SLO workbook
- `workbooks/cost-model.xlsx` — editable three-scenario cost model
- `app/` — small demo service
- `.github/workflows/deploy-azure.yml` — GitHub Actions deployment template
- `infra/main.bicep` — starter Azure infrastructure template

## Quick start locally
```bash
cd app
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Open `http://127.0.0.1:8000/health`.

## Before deploying to Azure
1. Create an Azure subscription/resource group and an Azure App Service Web App configured for Python.
2. Configure GitHub repository secrets for the deployment credentials required by the workflow (`AZURE_WEBAPP_PUBLISH_PROFILE`) and the app name (`AZURE_WEBAPP_NAME`). Download the publish profile from your Web App's Azure portal page.
3. Review the workflow and Azure pricing in your region. Never commit credentials, publish profiles, connection strings, or real secrets.
4. Enable Application Insights / Azure Monitor and verify alerts after deployment.
5. Treat the cost workbook as an estimate until verified in the Azure Pricing Calculator.

## Demo endpoints
- `/` — service info
- `/health` — health response
- `/ready` — readiness response

## Important scope note
This is a learning/demo starter. The sample's in-memory counter is not durable storage. The blueprint documents Blob Storage as the planned data tier; wire a storage SDK and managed identity before using persistent data. Do not present the demo as production-ready.
