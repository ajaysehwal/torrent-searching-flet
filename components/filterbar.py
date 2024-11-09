import flet as ft
from flet import Container, Row, Text, Icon, icons, padding, margin

def create_filters_bar() -> Container:
        return Container(
            content=Row(
                controls=[
                    Container(
                        content=Row(
                            controls=[
                                Icon(icons.FILTER_LIST_ROUNDED, color="#94a3b8", size=20),
                                Text("Filters", color="#94a3b8", size=14),
                            ],
                            spacing=4,
                        ),
                        on_click=lambda _: None,  # Add filter functionality
                        cursor=ft.CursorValue.POINTER,
                    ),
                    Container(  # Divider
                        bgcolor="#2d3748",
                        width=1,
                        height=24,
                        margin=margin.only(left=16, right=16),
                    ),
                    Row(  # Quality filters
                        controls=[
                            Container(
                                content=Text("4K", size=12),
                                bgcolor="#2d3748",
                                padding=padding.only(left=12, right=12, top=6, bottom=6),
                                border_radius=4,
                                on_click=lambda _: None,
                                cursor=ft.CursorValue.POINTER,
                            ),
                            Container(
                                content=Text("1080p", size=12),
                                bgcolor="#3b82f6",
                                padding=padding.only(left=12, right=12, top=6, bottom=6),
                                border_radius=4,
                                on_click=lambda _: None,
                                cursor=ft.CursorValue.POINTER,
                            ),
                            Container(
                                content=Text("720p", size=12),
                                bgcolor="#2d3748",
                                padding=padding.only(left=12, right=12, top=6, bottom=6),
                                border_radius=4,
                                on_click=lambda _: None,
                                cursor=ft.CursorValue.POINTER,
                            ),
                        ],
                        spacing=8,
                    ),
                ],
                alignment="center",
            ),
            padding=padding.only(left=24, right=24, top=12, bottom=12),
        )

