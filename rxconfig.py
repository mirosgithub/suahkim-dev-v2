import os

import reflex as rx


# Detect environment (dev, prod, or deployment)
ENV = os.getenv("ENV", os.getenv("ENVIRONMENT", "dev")).lower()
IS_DEV = ENV in ("dev", "development", "local")

# Port configuration with environment-aware defaults
# Development: Use alternative ports to avoid conflicts with running instances
# Production: Use standard ports (3000, 8080)
FRONTEND_PORT = int(
    os.getenv("REFLEX_FRONTEND_PORT", os.getenv("FRONTEND_PORT", "3001" if IS_DEV else "3000"))
)
BACKEND_PORT = int(os.getenv("BACKEND_PORT", "8081" if IS_DEV else "8080"))

# API URL configuration
# In development, use localhost with the configured backend port
# In production, use the provided API_URL or default to localhost:8080
if IS_DEV:
    API_URL = os.getenv("API_URL", f"http://localhost:{BACKEND_PORT}")
else:
    API_URL = os.getenv("API_URL", "http://localhost:8080")


config = rx.Config(
    app_name="suahkim_dev",
    api_url=API_URL,
    backend_port=BACKEND_PORT,
    frontend_port=FRONTEND_PORT,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)