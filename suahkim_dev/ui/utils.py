"""Utility functions for styling and component generation."""

from .styles import CLASS_NAMES


def get_text_class(variant: str = "primary") -> str:
    """Get text color class based on variant."""
    variants = {
        "primary": CLASS_NAMES["text_primary"],
        "secondary": CLASS_NAMES["text_secondary"],
        "tertiary": CLASS_NAMES["text_tertiary"],
    }
    return variants.get(variant, CLASS_NAMES["text_primary"])


def build_section_class(base: str = "") -> str:
    """Build section class name with optional base classes."""
    section_base = "min-h-screen flex items-center justify-center px-6 py-20 relative z-10"
    return f"{section_base} {base}".strip() if base else section_base


def build_glass_card_class(padding: str = "p-6") -> str:
    """Build glass card class name with optional padding."""
    return f"{CLASS_NAMES['liquid_glass']} {padding}"
