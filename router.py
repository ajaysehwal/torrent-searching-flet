import flet as ft
from pages import home, signin, signup, not_found
from typing import Callable
from utils.logger import setup_logger

logger = setup_logger()

class AppRouter:
    def __init__(self, page: ft.Page):
        self.page = page
        self.routes = {
            "/signin": signin.signin_page,
            "/signup": signup.signup_page,
            "/": home.home_page().main,
            "404": not_found.not_found_page
        }

    def route_guard(self, route: str, handler: Callable) -> None:
        """Executes the handler for the given route with basic guard logic (expandable)."""
        allowed_routes = ["/", "/signin", "/signup"]
        if route in allowed_routes:
            handler(self.page)
        else:
            self.routes["404"](self.page)

    def handle_routing(self, route: str) -> None:
        """Handle route changes with logging and error handling."""
        self.page.clean()
        
        try:
            handler = self.routes.get(route, self.routes["404"])
            self.route_guard(route, handler)
            self.page.update()
        except Exception as e:
            logger.error(f"Routing error for route '{route}': {str(e)}")
            self.page.go("/signin")  # Redirecting to signin on error
