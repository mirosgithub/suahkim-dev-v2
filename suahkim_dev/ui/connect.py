"""Reusable connect link component."""

import reflex as rx
from .card import glass_card
from .styles import CLASS_NAMES


def connect_link(
    icon_path: str,
    title: str,
    username: str,
    href: str,
    icon_size: int = 32,
    **kwargs
) -> rx.Component:
    """Create a connect link card with icon, title, and username.
    
    Args:
        icon_path: Path to the icon image (e.g., "/github.svg", "/linkedin.svg")
        title: Title text (e.g., "LinkedIn", "GitHub")
        username: Username/handle to display
        href: URL for the link
        icon_size: Size of the icon in pixels (default: 32)
        **kwargs: Additional props to pass to the link
    """
    content = rx.vstack(
        rx.image(
            src=icon_path,
            width=f"{icon_size}px",
            height=f"{icon_size}px",
            class_name="connect-icon mb-2",
        ),
        rx.heading(
            title,
            size="6",
            class_name=f"{CLASS_NAMES['text_tertiary']} mb-1"
        ),
        rx.text(
            username,
            size="4",
            class_name=CLASS_NAMES["text_secondary"]
        ),
        spacing="2",
        align="center",
    )
    
    return rx.link(
        glass_card(
            content,
            padding="p-8",
            width="100%",
            style={"minWidth": "320px", "maxWidth": "380px"},
        ),
        href=href,
        class_name="text-center",
        style={"textDecoration": "none"},
        **kwargs
    )
