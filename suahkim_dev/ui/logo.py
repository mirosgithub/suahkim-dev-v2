"""Reusable logo component."""

import reflex as rx
from .. import navigation


def logo(
    size: str = "2em",
    border_radius: str = "25%",
    on_click=None,
    **kwargs
) -> rx.Component:
    """Create a logo component that switches between light and dark variants.
    
    Args:
        size: Size of the logo (default: "2em")
        border_radius: Border radius for the logo (default: "25%")
        on_click: Optional click handler (defaults to navigation to home)
        **kwargs: Additional props to pass to the image
    """
    click_handler = on_click if on_click else navigation.NavState.to_home
    
    logo_style = {
        "cursor": "pointer",
        "flexShrink": "0",
        **kwargs.pop("style", {})
    }
    
    return rx.color_mode_cond(
        light=rx.image(
            src="/logo.png",
            width=size,
            height="auto",
            border_radius=border_radius,
            on_click=click_handler,
            style=logo_style,
            **kwargs
        ),
        dark=rx.image(
            src="/logo_dark.png",
            width=size,
            height="auto",
            border_radius=border_radius,
            on_click=click_handler,
            style=logo_style,
            **kwargs
        ),
    )
