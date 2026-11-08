# MediGuide AI — Deployment

## What was prepared
- Existing MediGuide multi-agent source retained.
- Added `api/index.py` as a Vercel-compatible FastAPI HTTP adapter.
- Added `vercel.json`.
- Removed `.env` and Git history from the deployment package.
- The local CLI and MCP server remain available for local/Docker use.

## Required Vercel environment variable
Set:
- `GOOGLE_API_KEY` = a newly generated Google AI API key

Do not commit `.env`.

## Deploy
```bash
git init
git add .
git commit -m "Prepare MediGuide AI for deployment"
git branch -M main
git remote add origin <YOUR_GITHUB_REPO_URL>
git push -u origin main
```

Then import the repository into Vercel and deploy.

API endpoints:
- `GET /api/`
- `GET /api/health`
- `POST /api/chat` with multipart form fields:
  - `query`
  - optional `image`

## Important architecture note
MediGuide's existing MCP server is a separate service. This Vercel adapter calls the ADK agent directly. If the production design must retain the MCP HTTP server as a separate runtime, deploy that service separately and configure `MCP_SERVER_URL`.
