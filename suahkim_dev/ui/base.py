import reflex as rx
from .nav import navbar


def base_page(child: rx.Component, hide_navbar=False, *args, **kwargs) -> rx.Component:
    """Base page wrapper with iOS 26 Liquid Glass theme"""
    if hide_navbar:
        return rx.box(
            child,
            rx.color_mode.button(position="bottom-left"),
            class_name="gradient-bg-light",
            width="100%",
            min_height="100vh",
            position="relative",
        )
    
    return rx.box(
        rx.fragment(
            navbar(),
            child,
        ),
        class_name="gradient-bg-light",
        width="100%",
        min_height="100vh",
        position="relative",
    )
