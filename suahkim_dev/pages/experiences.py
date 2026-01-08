import reflex as rx
from ..ui.section import section
from ..ui.experience_card import experience_card


def experiences_section() -> rx.Component:
    experiences = [
        {
            "company": "AKA Intelligence",
            "role": "Intern software developer",
            "description": "Implementing AI training data injection pipelines.",
        },
        {
            "company": "Self employed",
            "role": "Coding tutor",
            "description": "Teaching MATLAB and C programming for first-year engineering students.",
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
        rx.box(
            *experience_cards,
            class_name="responsive-grid-2",
            width="100%",
            style={"maxWidth": "56rem"},
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
        subtitle="Work that I genuinely enjoy"
    )