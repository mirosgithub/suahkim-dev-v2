import reflex as rx
from ..ui.section import section
from ..ui.contact import contact_link
from ..ui.styles import CLASS_NAMES


def contact_section() -> rx.Component:
    contacts = [
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
    
    contact_links = [
        contact_link(
            icon_path=contact["icon"],
            title=contact["title"],
            username=contact["username"],
            href=contact["href"],
        )
        for contact in contacts
    ]
    
    content = rx.vstack(
        rx.desktop_only(
            rx.hstack(
                *contact_links,
                spacing="6",
                width="100%",
                style={"maxWidth": "48rem"},
            ),
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                *contact_links,
                spacing="6",
                width="100%",
                style={"maxWidth": "32rem"},
            ),
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
        section_id="contact",
        title="Connect",
        subtitle="Explore my work and get in touch",
    )

