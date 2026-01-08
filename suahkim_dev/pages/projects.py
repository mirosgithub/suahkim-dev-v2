import reflex as rx
from ..ui.section import section
from ..ui.project_card import project_card


def projects_section() -> rx.Component:
    projects = [
        {
            "title": "Portfolio website v.2",
            "category": "Web app",
            "description": "Second iteration of my portfolio website, built with Reflex to explore Python-based web frameworks.",
            "tags": ["Python", "Reflex", "CSS", "Docker", "Cloud Run"],
        },
        {
            "title": "Emoji processor",
            "category": "Mini tool",
            "description": "Tool to extract and process emojis from image sheets for use as custom Notion emojis.",
            "tags": ["Python", "OpenCV"],
        },
        {
            "title": "Lullab.ai",
            "category": "AI web app",
            "description": "Generates and narrates personalised bedtime stories for children and adults. Backend developer on 1st place team.",
            "tags": ["Python", "Flask", "Gemini API", "Docker", "Cloud Run"],
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
        subtitle="Coding something cool every day",
    )

