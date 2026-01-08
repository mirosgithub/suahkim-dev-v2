import reflex as rx
from ..ui.section import section
from ..ui.project_card import project_card


def projects_section() -> rx.Component:
    projects = [
        {
            "title": "Title",
            "category": "Category",
            "description": "Description",
            "tags": ["Stack1", "Stack2", "Stack3"],
        },
        {
            "title": "Title",
            "category": "Category",
            "description": "Description",
            "tags": ["Stack1", "Stack2", "Stack3"],
        },
        {
            "title": "Title",
            "category": "Category",
            "description": "Description",
            "tags": ["Stack1", "Stack2", "Stack3"],
        },
    ]
    
    project_cards = [
        project_card(
            title=project["title"],
            category=project["category"],
            description=project["description"],
            tags=project["tags"],
        )
        for project in projects
    ]
    
    content = rx.vstack(
        rx.grid(
            *project_cards,
            columns="3",
            spacing="6",
            width="100%",
            style={"maxWidth": "80rem"},
        ),
        spacing="8",
        align="center",
        justify="center",
        width="100%",
    )
    
    return section(
        content,
        section_id="projects",
        title="Projects",
        subtitle="Subheading",
    )

