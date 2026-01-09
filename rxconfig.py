import os

import reflex as rx


config = rx.Config(
    app_name="suahkim_dev",
    api_url=os.getenv("API_URL", "http://localhost:8080"),
    backend_port=int(os.getenv("BACKEND_PORT", "8080")),
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)