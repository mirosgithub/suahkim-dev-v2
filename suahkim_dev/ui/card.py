"""Reusable glass card component."""

import reflex as rx
from .styles import CLASS_NAMES


def glass_card(
    children: rx.Component | list[rx.Component],
    padding: str = "p-6",
    width: str = "100%",
    height: str | None = None,
    additional_class: str = "",
    **kwargs
) -> rx.Component:
    """Create a glass card with liquid glass styling.
    
    Args:
        children: Content to display in the card
        padding: Padding class (default: "p-6")
        width: Width of the card (default: "100%")
        height: Optional height of the card
        additional_class: Additional CSS classes to append
        **kwargs: Additional props to pass to the card container
    """
    card_class = f"{CLASS_NAMES['liquid_glass']} {padding}"
    if additional_class:
        card_class = f"{card_class} {additional_class}"
    
    style = kwargs.pop("style", {})
    style["width"] = width
    if height:
        style["height"] = height
    
    # Handle children - if it's a list, use it directly; otherwise wrap in list
    if isinstance(children, list):
        card_children = children
    else:
        card_children = [children]
    
    return rx.box(
        *card_children,
        class_name=card_class,
        style=style,
        **kwargs
    )
