from flet import Container,Row,Icon,Text,icons,IconButton,padding,colors,BlurTileMode,BoxShadow,Blur,Offset,Page
def create_navbar(page:Page):
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
                    # Right section
                    Row(
                        controls=[
                            Container(
                                content=IconButton(
                                    icon=icons.SETTINGS,
                                    icon_size=24,
                                    icon_color=colors.WHITE,

                                    on_click=lambda _: print("Setting clicked"),
                                ),
                            ),
                            Container(width=5),
                            Container(
                                content=Row(
                                    controls=[
                                        Icon(icons.PERSON_OUTLINE_ROUNDED, 
                                             color="white",
                                             size=20),
                                        Text("Sign Up", 
                                             color="white",
                                             size=14,
                                             weight="w500")
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
                                        Icon(icons.PERSON_OUTLINE_ROUNDED, 
                                             color="white",
                                             size=20),
                                        Text("Sign In", 
                                             color="white",
                                             size=14,
                                             weight="w500")
                                    ],
                                    spacing=5
                                ),
                                on_click=lambda _: page.go('/signin'),
                                padding=padding.only(left=15, right=15, top=8, bottom=8),
                                bgcolor=colors.TRANSPARENT
                            ),
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