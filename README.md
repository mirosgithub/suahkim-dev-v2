# suahkim-dev-v2

[![Deploy to Cloud Run](https://github.com/mirosgithub/suahkim-dev-v2/actions/workflows/deploy-cloudrun.yml/badge.svg?branch=main)](https://github.com/mirosgithub/suahkim-dev-v2/actions/workflows/deploy-cloudrun.yml)

Personal site built with [Reflex](https://reflex.dev/), deployed to Google Cloud Run.

## Deployment

Deploys on pushes to `main` via GitHub Actions (see the workflow badge above).

## Local development

Prereqs: Python 3.14 and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
uv run reflex run
```

### Environment Configuration

The app automatically detects the environment and adjusts ports accordingly:

- **Development mode** (default): Uses ports 3001 (frontend) and 8081 (backend) to avoid conflicts
- **Production mode**: Uses ports 3000 (frontend) and 8080 (backend)

To switch between modes, set the `ENV` environment variable:

```bash
# Development (default)
ENV=dev uv run reflex run

# Production mode
ENV=prod uv run reflex run
```

You can also create a `.env` file (see `.env.example`) to set custom ports:

```bash
# Copy the example file
cp .env.example .env

# Edit .env to customise ports
FRONTEND_PORT=3001
BACKEND_PORT=8081
```

**Note**: Reflex will automatically use the next available port if your specified port is already in use (development mode only).
