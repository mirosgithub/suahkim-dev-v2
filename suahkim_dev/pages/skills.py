import reflex as rx
from ..ui.section import section
from ..ui.skill_category_card import skill_category_card


def skills_section() -> rx.Component:
    skill_categories = [
        {
            "category": "Machine languages",
            "skills": [
                {"name": "Python", "level": 90},
                {"name": "Java", "level": 60},
                {"name": "C", "level": 30},
                {"name": "Bash", "level": 80},
            ],
        },
        {
            "category": "Human languages",
            "skills": [
                {"name": "English", "level": 80},
                {"name": "Korean", "level": 90},
                {"name": "Chinese", "level": 60},
                {"name": "Latin", "level": 30},
            ],
        },
        {
            "category": "Devtools",
            "skills": [
                {"name": "Docker", "level": 60},
                {"name": "Google Cloud", "level": 70},
                {"name": "Git", "level": 90},
                {"name": "Terminal", "level": 80},
            ],
        },
        {
            "category": "Frameworks",
            "skills": [
                {"name": "Reflex", "level": 80},
                {"name": "UV", "level": 90},
                {"name": "Django", "level": 70},
                {"name": "Flask", "level": 60},
            ],
        },
        
    ]
    
    category_cards = [
        skill_category_card(
            category=cat["category"],
            skills=cat["skills"],
        )
        for cat in skill_categories
    ]
    
    content = rx.vstack(
        rx.box(
            *category_cards,
            class_name="responsive-grid-2",
            width="100%",
            style={"maxWidth": "72rem"},
        ),
        spacing="8",
        align="center",
        justify="center",
        width="100%",
    )
    
    return section(
        content,
        section_id="skills",
        title="Skills",
        subtitle="My ever-growing toolkit",
    )

