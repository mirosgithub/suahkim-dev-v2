import reflex as rx
from . import routes

class NavState(rx.State):
    def to_home(self):
        return rx.redirect(routes.HOME)
    
    def to_experiences(self):
        return rx.redirect(routes.EXPERIENCES)
    
    def scroll_to_section(self, section_id: str):
        return rx.eval(f"document.getElementById('{section_id}')?.scrollIntoView({{behavior: 'smooth', block: 'start'}})")