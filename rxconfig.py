import reflex as rx

config = rx.Config(
    app_name="suahkim_dev",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)