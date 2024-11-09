import flet as ft
from flet import Container, Row, Column, Text, Image, ImageFit, IconButton, icons, padding, margin, animation

def create_movie_row(movie, on_click, on_download=None) -> Container:
    return Container(
        content=Row(
            controls=[
                # Poster and basic info
                Container(
                    content=Row(
                        controls=[
                            Image(
                                src=movie.poster if movie.poster != "N/A" else "/placeholder.png",
                                width=80,
                                height=120,
                                fit=ImageFit.COVER,
                                border_radius=8,
                            ),
                            Column(
                                controls=[
                                    Container(
                                        content=Column(
                                            controls=[
                                                Text(
                                                    movie.title,
                                                    size=16,
                                                    weight="bold",
                                                    color="white",
                                                ),
                                                Row(
                                                    controls=[
                                                        Container(
                                                            content=Text(
                                                                movie.year,
                                                                size=12,
                                                                color="#94a3b8",
                                                            ),
                                                        ),
                                                        Container(
                                                            content=Text(
                                                                "•",
                                                                size=12,
                                                                color="#94a3b8",
                                                            ),
                                                            margin=margin.only(left=8, right=8),
                                                        ),
                                                        Container(
                                                            content=Text(
                                                                movie.runtime or "N/A",
                                                                size=12,
                                                                color="#94a3b8",
                                                            ),
                                                        ),
                                                    ],
                                                    spacing=0,
                                                ),
                                            ],
                                            spacing=4,
                                        ),
                                        padding=padding.only(left=16),
                                    ),
                                ],
                                expand=True,
                            ),
                        ],
                        spacing=0,
                    ),
                    expand=True,
                ),
                
                # Stats and quality
                Row(
                    controls=[
                        Column(
                            controls=[
                                Row(
                                    controls=[
                                        IconButton(
                                            icons.STAR_ROUNDED,
                                            color="#fbbf24",
                                            size=16,
                                        ),
                                        Text(
                                            movie.rating or "N/A",
                                            size=14,
                                            weight="w500",
                                            color="white",
                                        ),
                                    ],
                                    spacing=4,
                                ),
                                Container(height=4),
                                Text(
                                    movie.size or "N/A",
                                    size=12,
                                    color="#94a3b8",
                                ),
                            ],
                            horizontal_alignment="center",
                        ),
                        Container(width=24),  # Spacer
                        Column(
                            controls=[
                                Row(
                                    controls=[
                                        IconButton(
                                            icons.ARROW_UPWARD_ROUNDED,
                                            color="#22c55e",
                                            size=16,
                                        ),
                                        Text(
                                            str(movie.seeds) if movie.seeds is not None else "0",
                                            size=14,
                                            color="#22c55e",
                                        ),
                                    ],
                                    spacing=4,
                                ),
                                Row(
                                    controls=[
                                        IconButton(
                                            icons.ARROW_DOWNWARD_ROUNDED,
                                            color="#ef4444",
                                            size=16,
                                        ),
                                        Text(
                                            str(movie.peers) if movie.peers is not None else "0",
                                            size=14,
                                            color="#ef4444",
                                        ),
                                    ],
                                    spacing=4,
                                ),
                            ],
                            spacing=4,
                        ),
                        Container(width=24),  # Spacer
                        Container(
                            content=Text(
                                movie.quality or "SD",
                                size=12,
                                weight="w500",
                            ),
                            bgcolor="#3b82f6",
                            padding=padding.only(left=12, right=12, top=6, bottom=6),
                            border_radius=4,
                        ),
                        Container(width=16),  # Spacer
                        IconButton(
                            icon=icons.DOWNLOAD_ROUNDED,
                            icon_size=20,
                            icon_color="#3b82f6",
                            bgcolor="#1e293b",
                            on_click=lambda e: on_download(movie) if on_download else None,
                        ),
                    ],
                    alignment="center",
                ),
            ],
            alignment="spaceBetween",
        ),
        bgcolor="#1e293b",
        border_radius=12,
        padding=padding.all(16),
        margin=margin.only(bottom=8),
        ink=True,
        on_click=lambda e: on_click(movie),
        animate=animation.Animation(300, "easeOut"),
    )
