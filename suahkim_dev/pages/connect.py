import reflex as rx
from ..ui.section import section
from ..ui.connect import connect_link
from ..ui.styles import CLASS_NAMES


def connect_section() -> rx.Component:
    connections = [
        {
            "icon": "/linkedin.svg",
            "title": "LinkedIn",
            "username": "@Suah Kim",
            "href": "https://linkedin.com/in/suah-adela-kim",
        },
        {
            "icon": "/github.svg",
            "title": "GitHub",
            "username": "@mirosgithub",
            "href": "https://github.com/mirosgithub",
        },
    ]
    
    connect_links = [
        connect_link(
            icon_path=connection["icon"],
            title=connection["title"],
            username=connection["username"],
            href=connection["href"],
        )
        for connection in connections
    ]
    
    content = rx.vstack(
        rx.flex(
            *connect_links,
            spacing="6",
            wrap="wrap",
            justify="center",
            align="center",
            width="100%",
            style={"maxWidth": "64rem"},
        ),
        rx.text(
            "© 2026 Suah Kim.",
            size="3",
            class_name=f"{CLASS_NAMES['text_secondary']} text-center mt-16",
        ),
        spacing="8",
        align="center",
        justify="center",
        width="100%",
    )
    
    return section(
        content,
        section_id="connect",
        title="Connect",
        subtitle="Explore my work and get in touch",
    )

