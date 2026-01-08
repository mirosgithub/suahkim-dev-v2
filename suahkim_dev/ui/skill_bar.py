"""Reusable skill bar component."""

import reflex as rx
from .styles import CLASS_NAMES


def skill_bar(name: str, level: int) -> rx.Component:
    """Create a skill bar with name and proficiency level.
    
    Args:
        name: Skill name
        level: Proficiency level (0-100)
    """
    return rx.vstack(
        rx.hstack(
            rx.text(name, class_name=CLASS_NAMES["text_tertiary"]),
            rx.text(f"{level}%", class_name=CLASS_NAMES["text_secondary"]),
            justify="between",
            width="100%",
        ),
        rx.box(
            rx.box(
                width=f"{level}%",
                height="100%",
                background="linear-gradient(to right, #6b7280, #9ca3af)",
                border_radius="9999px",
            ),
            width="100%",
            height="0.5rem",
            background="rgba(255, 255, 255, 0.6)",
            border_radius="9999px",
            overflow="hidden",
        ),
        spacing="2",
        width="100%",
    )
