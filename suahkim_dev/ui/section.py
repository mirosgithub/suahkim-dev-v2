"""Reusable section wrapper component."""

import reflex as rx
from .header import section_header


def section(
    content: rx.Component,
    section_id: str | None = None,
    title: str | None = None,
    subtitle: str | None = None,
    **kwargs
) -> rx.Component:
    """Create a standardised section wrapper with optional header.
    
    Args:
        content: Main content of the section
        section_id: Optional ID for the section (for navigation)
        title: Optional section title
        subtitle: Optional section subtitle
        **kwargs: Additional props to pass to the section
    """
    children = []
    
    # Add header if title is provided
    if title:
        children.append(section_header(title, subtitle))
    
    # Add content
    if isinstance(content, list):
        children.extend(content)
    else:
        children.append(content)
    
    # Wrap in vstack if multiple children
    if len(children) > 1:
        inner_content = rx.vstack(
            *children,
            spacing="8",
            align="center",
            justify="center",
            width="100%",
        )
    else:
        inner_content = children[0] if children else content
    
    return rx.section(
        inner_content,
        class_name="min-h-screen flex items-center justify-center px-6 py-20 relative z-10",
        width="100%",
        id=section_id,
        **kwargs
    )
