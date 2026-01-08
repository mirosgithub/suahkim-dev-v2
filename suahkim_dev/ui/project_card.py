"""Reusable project card component."""

import reflex as rx
from .card import glass_card
from .styles import CLASS_NAMES


def project_card(
    title: str,
    category: str,
    description: str,
    tags: list[str],
    **kwargs
) -> rx.Component:
    """Create a project card with title, category, description, and tags.
    
    Args:
        title: Project title
        category: Project category
        description: Project description
        tags: List of technology tags
        **kwargs: Additional props to pass to the card
    """
    return glass_card(
        rx.vstack(
            rx.vstack(
                rx.heading(
                    title,
                    size="6",
                    class_name=f"{CLASS_NAMES['text_tertiary']} mb-1 project-title",
                    style={"maxWidth": "100%", "overflow": "hidden"},
                ),
                rx.text(
                    category,
                    size="3",
                    class_name="text-purple-600 dark:text-purple-400 project-category",
                ),
                spacing="1",
                align="start",
                width="100%",
            ),
            rx.text(
                description,
                size="4",
                class_name=f"{CLASS_NAMES['text_secondary']} mb-4 project-description",
            ),
            rx.box(
                rx.hstack(
                    *[
                        rx.box(
                            rx.text(tag, size="2"),
                            padding="0.25rem 0.75rem",
                            border_radius="9999px",
                            background="rgba(255, 255, 255, 0.2)",
                            class_name=f"{CLASS_NAMES['text_tertiary']} project-tag",
                        )
                        for tag in tags
                    ],
                    spacing="2",
                    wrap="wrap",
                    justify="center",
                    width="100%",
                ),
                width="100%",
            ),
            spacing="4",
            align="start",
            width="100%",
        ),
        padding="p-6",
        width="100%",
        height="100%",
        **kwargs
    )
