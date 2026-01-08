"""Style constants and common style dictionaries for the application."""

# Common color values
COLORS = {
    "text_primary_light": "#1f2937",
    "text_primary_dark": "rgba(243, 244, 246, 1)",
    "text_secondary_light": "#374151",
    "text_secondary_dark": "rgba(243, 244, 246, 1)",
    "text_tertiary_light": "#6b7280",
    "text_tertiary_dark": "rgba(156, 163, 175, 1)",
    "text_purple_light": "#9333ea",
    "text_purple_dark": "#a855f7",
}

# Common spacing values
SPACING = {
    "xs": "0.25rem",
    "sm": "0.5rem",
    "md": "1rem",
    "lg": "1.5rem",
    "xl": "2rem",
    "2xl": "3rem",
}

# Glass effect styles
GLASS_STYLE = {
    "background": "rgba(255, 255, 255, 0.4)",
    "backdrop_filter": "blur(24px)",
    "-webkit-backdrop-filter": "blur(24px)",
    "border": "1px solid rgba(255, 255, 255, 0.5)",
    "box_shadow": "0 25px 50px -12px rgba(0, 0, 0, 0.25)",
    "border_radius": "32px",
}

GLASS_DARK_STYLE = {
    "background": "rgba(40, 40, 45, 0.4)",
    "backdrop_filter": "blur(24px)",
    "-webkit-backdrop-filter": "blur(24px)",
    "border": "1px solid rgba(60, 60, 65, 0.5)",
    "box_shadow": "0 25px 50px -12px rgba(0, 0, 0, 0.5)",
    "border_radius": "32px",
}

# Section wrapper styles
SECTION_WRAPPER_STYLE = {
    "min_height": "100vh",
    "display": "flex",
    "align_items": "center",
    "justify_content": "center",
    "padding_x": "1.5rem",
    "padding_y": "5rem",
    "position": "relative",
    "z_index": "10",
    "width": "100%",
}

# Typography settings
TYPOGRAPHY = {
    "font_family": "var(--font-heading)",
    "heading_size_9": "9",
    "heading_size_6": "6",
    "text_size_5": "5",
    "text_size_4": "4",
    "text_size_3": "3",
}

# Common class name combinations
CLASS_NAMES = {
    "section_title": "text-gray-900 dark:text-white mb-4 text-center",
    "section_subtitle": "text-gray-600 dark:text-gray-400 text-center mb-12",
    "text_primary": "text-gray-900 dark:text-white",
    "text_secondary": "text-gray-600 dark:text-gray-400",
    "text_tertiary": "text-gray-700 dark:text-gray-300",
    "liquid_glass": "liquid-glass",
}
