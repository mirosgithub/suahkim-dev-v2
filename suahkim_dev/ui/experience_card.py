"""Reusable experience card component."""

import reflex as rx
from .card import glass_card
from .styles import CLASS_NAMES


def experience_card(
    company: str,
    role: str,
    description: str,
    **kwargs
) -> rx.Component:
    """Create an experience card with company, role, and description.
    
    Args:
        company: Company name
        role: Job role/title
        description: Job description
        **kwargs: Additional props to pass to the card
    """
    return glass_card(
        rx.vstack(
            rx.heading(
                role,
                size="6",
                class_name=CLASS_NAMES['text_tertiary']
            ),
            rx.text(
                company,
                size="5",
                class_name=CLASS_NAMES['text_secondary']
            ),
            rx.text(
                description,
                size="5",
                class_name=CLASS_NAMES["text_secondary"]
            ),
            spacing="2",
            align="start",
            width="100%",
        ),
        padding="p-8",
        width="100%",
        **kwargs
    )
