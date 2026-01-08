import reflex as rx
from ..ui.section import section
from ..ui.experience_card import experience_card


def experiences_section() -> rx.Component:
    experiences = [
        {
            "company": "Company",
            "role": "Role",
            "description": "Description",
        },
        {
            "company": "Company",
            "role": "Role",
            "description": "Description",
        },
    ]
    
    experience_cards = [
        experience_card(
            company=exp["company"],
            role=exp["role"],
            description=exp["description"],
        )
        for exp in experiences
    ]
    
    content = rx.vstack(
        rx.grid(
            *experience_cards,
            columns="2",
            spacing="8",
            width="100%",
            style={"maxWidth": "72rem"},
        ),
        spacing="8",
        align="center",
        justify="center",
        width="100%",
    )
    
    return section(
        content,
        section_id="experiences",
        title="Experiences",
    )