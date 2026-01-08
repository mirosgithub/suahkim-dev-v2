"""Reusable skill category card component."""

import reflex as rx
from .card import glass_card
from .skill_bar import skill_bar
from .styles import CLASS_NAMES


def skill_category_card(
    category: str,
    skills: list[dict[str, int | str]],
    **kwargs
) -> rx.Component:
    """Create a skill category card with multiple skill bars.
    
    Args:
        category: Category name
        skills: List of skill dictionaries with 'name' and 'level' keys
        **kwargs: Additional props to pass to the card
    """
    skill_items = [
        skill_bar(skill["name"], skill["level"])
        for skill in skills
    ]
    
    return glass_card(
        rx.vstack(
            rx.heading(
                category,
                size="6",
                class_name=f"{CLASS_NAMES['text_tertiary']} mb-1"
            ),
            rx.vstack(*skill_items, spacing="6", width="100%"),
            spacing="4",
            align="start",
            width="100%",
        ),
        padding="p-8",
        width="100%",
        **kwargs
    )
