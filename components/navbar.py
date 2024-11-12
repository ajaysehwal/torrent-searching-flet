from flet import (
    Container, Row, Icon, Text, icons, IconButton, padding, colors,
    BlurTileMode, BoxShadow, Blur, Offset, Page, PopupMenuButton,
    PopupMenuItem
)
from services.AuthServices import auth

def create_navbar(page: Page):
    isauth = auth().is_authenticated()
    
    def handle_logout(e):
        auth().logout()
        page.go('/signin')
        page.update()
    
    def toggle_theme(e):
        e.control.checked = not e.control.checked
        # Add your theme toggle logic here
        page.theme_mode = "dark" if e.control.checked else "light"
        page.update()

    return Container(
            content=Row(
                controls=[
                    # Logo section
                    Row(
                        controls=[
                            Icon(
                                icons.MOVIE_FILTER_ROUNDED,
                                size=30,
                                color="#3b82f6"
                            ),
                            Text(
                                "TorrentFlix",
                                size=24,
                                weight="bold",
                                color="white",
                                font_family="Poppins"
                            ),
                        ],
                        spacing=10,
                    ),
                    # Spacer
                    Container(expand=True),
                    Row(
                        controls=[
                            Container(width=5),
                            PopupMenuButton(
                                items=[
                                    PopupMenuItem(
                                        content=Row(
                                            controls=[
                                                Icon(
                                                    icons.PERSON_OUTLINE_ROUNDED,
                                                    color=colors.WHITE,
                                                    size=20
                                                ),
                                                Text(
                                                    "Account",
                                                    color=colors.WHITE,
                                                    weight="w500"
                                                ),
                                            ]
                                        ),
                                        on_click=lambda _: page.go('/profile')
                                    ),
                                    PopupMenuItem(
                                        content=Row(
                                            controls=[
                                                Icon(
                                                    icons.DARK_MODE_OUTLINED,
                                                    color=colors.BLACK,
                                                    size=20
                                                ),
                                                Text(
                                                    "Dark Mode",
                                                    color=colors.BLACK,
                                                    weight="w500"
                                                ),
                                            ]
                                        ),
                                        checked=page.theme_mode == "dark",
                                        on_click=toggle_theme
                                    ),
                                    PopupMenuItem(),  # divider
                                    PopupMenuItem(
                                        content=Row(
                                            controls=[
                                                Icon(
                                                    icons.LOGOUT_ROUNDED,
                                                    color=colors.BLACK,
                                                    size=20
                                                ),
                                                Text(
                                                    "Logout",
                                                    color=colors.BLACK,
                                                    weight="w500"
                                                ),
                                            ]
                                        ),
                                        on_click=handle_logout
                                    ),
                                ],
                                content=Container(
                                    content=Row(
                                        controls=[
                                            Icon(
                                                icons.ACCOUNT_CIRCLE_ROUNDED,
                                                color=colors.WHITE,
                                                size=24
                                            ),
                                            Text(
                                                "Account",
                                                color=colors.WHITE,
                                                size=14,
                                                weight="w500"
                                            ),
                                            Icon(
                                                icons.ARROW_DROP_DOWN_ROUNDED,
                                                color=colors.WHITE
                                            )
                                        ],
                                        spacing=5
                                    ),
                                    padding=padding.only(left=15, right=15, top=8, bottom=8),
                                )
                            ) if isauth else Row(
                                controls=[
                                    Container(
                                        content=Row(
                                            controls=[
                                                Icon(
                                                    icons.PERSON_OUTLINE_ROUNDED,
                                                    color="white",
                                                    size=20
                                                ),
                                                Text(
                                                    "Sign Up",
                                                    color="white",
                                                    size=14,
                                                    weight="w500"
                                                )
                                            ],
                                            spacing=5
                                        ),
                                        on_click=lambda _: page.go('/signup'),
                                        padding=padding.only(left=15, right=15, top=8, bottom=8),
                                        bgcolor="#3b82f6"
                                    ),
                                    Container(
                                        content=Row(
                                            controls=[
                                                Icon(
                                                    icons.PERSON_OUTLINE_ROUNDED,
                                                    color="white",
                                                    size=20
                                                ),
                                                Text(
                                                    "Sign In",
                                                    color="white",
                                                    size=14,
                                                    weight="w500"
                                                )
                                            ],
                                            spacing=5
                                        ),
                                        on_click=lambda _: page.go('/signin'),
                                        padding=padding.only(left=15, right=15, top=8, bottom=8),
                                        bgcolor=colors.TRANSPARENT
                                    ),
                                ],
                                spacing=10,
                            )
                        ],
                        spacing=10,
                    ),
                ],
                alignment="center",
            ),
            padding=padding.only(left=20, right=20, top=15, bottom=15),
            bgcolor=colors.with_opacity(0.8, "#1e293b"),
            blur=Blur(20, 20, BlurTileMode.MIRROR),
            shadow=BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=colors.with_opacity(0.2, "black"),
                offset=Offset(0, 2),
            ),
        )