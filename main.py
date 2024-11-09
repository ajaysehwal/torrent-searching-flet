import flet as ft
from flet import *
from utils.logger import setup_logger
logger = setup_logger()
OMDB_API_URL = "http://www.omdbapi.com/"
OMDB_API_KEY = "494e9276"
from router import AppRouter
def main(page: ft.Page):
    page.padding = 0
    page.spacing = 0
    def error_boundary(error: Exception):
        logger.error(f"Application error: {str(error)}")
        page.clean()
        page.add(
            ft.Text("An error occurred. Please try again later.", color="red"),
            ft.ElevatedButton("Reload", on_click=lambda _: page.clean())
        )
        page.update()
    try:
       router = AppRouter(page)
       def route_change(e):
           logger.info(f"Route Change Triggered | New Route: {e.route}")
           router.handle_routing(e.route)
           
       page.on_route_change = route_change
       initial_route = "/" 
       page.go(initial_route)
    except Exception as e:
        error_boundary(e)


    page.update()


ft.app(target=main)
