import reflex as rx
from .logo import logo


# Navigation links data
NAV_LINKS = [
    {"text": "Home", "section_id": "home"},
    {"text": "Experiences", "section_id": "experiences"},
    {"text": "Projects", "section_id": "projects"},
    {"text": "Skills", "section_id": "skills"},
    {"text": "Connect", "section_id": "connect"},
]


def navbar_link(text: str, section_id: str, is_active: bool = False) -> rx.Component:
    """iOS 26 style navbar link with glass effect - scrolls to section"""
    link_style = {
        "padding": "0.5rem 1.5rem",
        "border_radius": "9999px",
        "color": "#374151",
        "cursor": "pointer",
    }
    
    if is_active:
        link_style.update({
            "background": "linear-gradient(to right, #2563eb, #9333ea)",
            "color": "white",
            "box_shadow": "0 10px 15px -3px rgba(0, 0, 0, 0.1)",
        })
    else:
        link_style.update({
            "color": "#374151",
        })
    
    return rx.link(
        rx.text(text, size="4", weight="medium"),
        href=f"#{section_id}",
        style=link_style,
    )


def navbar() -> rx.Component:
    """iOS 26 style glass navigation bar"""
    nav_style = {
        "background": "rgba(255, 255, 255, 0.4)",
        "backdrop_filter": "blur(24px)",
        "-webkit-backdrop-filter": "blur(24px)",
        "border": "1px solid rgba(255, 255, 255, 0.5)",
        "box_shadow": "0 25px 50px -12px rgba(0, 0, 0, 0.25)",
        "border_radius": "9999px",
        "padding": "0.75rem 1.5rem",
        "position": "fixed",
        "top": "1.5rem",
        "left": "50%",
        "transform": "translateX(-50%)",
        "z_index": "50",
    }
    
    # Generate menu items from NAV_LINKS
    menu_items = [
        rx.menu.item(
            rx.link(
                link["text"],
                href=f"#{link['section_id']}",
                style={"color": "inherit", "textDecoration": "none"},
            ),
        )
        for link in NAV_LINKS
    ]
    
    return rx.box(
        rx.desktop_only(
            rx.box(
                rx.hstack(
                    logo(size="2em"),
                    *[navbar_link(link["text"], link["section_id"]) for link in NAV_LINKS],
                    rx.color_mode.button(
                        class_name="theme-toggle-icon-button",
                    ),
                    spacing="2",
                    align_items="center",
                ),
                style=nav_style,
                class_name="glass-navbar",
            )
        ),
        rx.mobile_and_tablet(
            rx.box(
                rx.hstack(
                    rx.menu.root(
                        rx.menu.trigger(
                            rx.icon("menu", size=24, class_name="menu-icon-navbar"),
                            class_name="menu-trigger-mobile",
                        ),
                        rx.menu.content(*menu_items),
                    ),
                    logo(
                        size="1.75rem",
                        style={"flex": "1", "textAlign": "center", "objectFit": "contain"},
                    ),
                    rx.color_mode.button(
                        class_name="theme-toggle-icon-button",
                    ),
                    justify="between",
                    align_items="center",
                    width="100%",
                ),
                style={**nav_style, "width": "calc(100% - 2rem)", "padding": "0.75rem 1rem"},
                class_name="glass-navbar",
            )
        ),
    )
