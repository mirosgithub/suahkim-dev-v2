import reflex as rx

from .ui.base import base_page
from .pages import hero, experiences, projects, skills, connect


def index() -> rx.Component:
    content = rx.vstack(
        hero.hero_section(),
        experiences.experiences_section(),
        projects.projects_section(),
        skills.skills_section(),
        connect.connect_section(),
        spacing="0",
        width="100%",
        position="relative",
        z_index="10",
    )
    return base_page(content)

app = rx.App(stylesheets=["/styles.css"])
app.add_page(index)