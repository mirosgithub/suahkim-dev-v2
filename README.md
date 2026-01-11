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
