import reflex as rx
from ..ui.card import glass_card
from ..ui.section import section


def hero_section() -> rx.Component:
    content = glass_card(
        rx.vstack(
            rx.heading(
                "Suah Kim",
                size="9",
                class_name="text-gray-900 dark:text-white mb-2 hero-name",
                style={"fontFamily": "var(--font-heading)"},
            ),
            rx.heading(
                "Intern Software Developer | Software Engineering Student",
                size="6",
                class_name="text-gray-700 dark:text-gray-300 mb-4 text-center",
            ),
            rx.text(
                "Seoul, Korea ...✈ Auckland, New Zealand",
                size="5",
                class_name="text-gray-600 dark:text-gray-400 max-w-2xl text-center",
            ),
            spacing="4",
            align="center",
        ),
        padding="p-6 sm:p-12",
        width="100%",
        style={"maxWidth": "56rem"},
    )
    
    return section(
        content,
        section_id="home",
    )

