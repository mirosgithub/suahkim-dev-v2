"""Reusable section header component."""

import reflex as rx
from .styles import TYPOGRAPHY, CLASS_NAMES


def section_header(
    title: str,
    subtitle: str | None = None,
    title_size: str = "9",
    subtitle_size: str = "6",
    **kwargs
) -> rx.Component:
    """Create a standardised section header with optional subtitle.
    
    Args:
        title: Main heading text
        subtitle: Optional subtitle text
        title_size: Size of the title heading (default: "9")
        subtitle_size: Size of the subtitle text (default: "6")
        **kwargs: Additional props to pass to the container
    """
    children = [
        rx.heading(
            title,
            size=title_size,
            class_name=f"{CLASS_NAMES['section_title']} px-4",
            style={"fontFamily": TYPOGRAPHY["font_family"]},
        )
    ]
    
    if subtitle:
        children.append(
            rx.text(
                subtitle,
                size=subtitle_size,
                class_name=CLASS_NAMES["section_subtitle"],
            )
        )
    
    return rx.vstack(
        *children,
        spacing="8",
        align="center",
        justify="center",
        **kwargs
    )
