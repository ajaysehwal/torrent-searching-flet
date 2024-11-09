import flet as ft
def create_search_bar() -> ft.Container:
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.icons.SEARCH_ROUNDED,
                        icon_color="#94a3b8",
                        icon_size=20,
                    ),
                    ft.TextField(
                        border=ft.InputBorder.NONE,
                        hint_text="Search movies, series, or anime...",
                        hint_style=ft.TextStyle(
                            color="#94a3b8",
                            size=14,
                        ),
                        text_style=ft.TextStyle(
                            color="white",
                            size=14,
                        ),
                        expand=True,
                        content_padding=ft.padding.only(top=8, bottom=8),
                    ),
                ],
                spacing=10,
            ),
            bgcolor="#1e293b",
            border_radius=8,
            padding=ft.padding.only(left=16, right=16),
        )

