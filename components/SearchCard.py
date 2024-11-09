from flet import *

def create_search_result_card(result: dict, show_details, handle_download,page:Page) -> Container:
    """Create a responsive search result card with modern design and horizontal info chips"""
    title_text=Text(
                     result.get("Title", "Unknown"),
                     size=18,
                     color=colors.BLACK,
                     weight="bold",
                                    )
    def adjust_text_size(e):
        if page.width < 400:
            title_text.size = 14  # Smaller text for small screens
        elif page.width < 600:
            title_text.size = 16  # Medium size for mid-sized screens
        else:
            title_text.size = 18  # Default size for larger screens
        page.update()  # Update to apply changes
    adjust_text_size(None)
    page.on_resized = adjust_text_size


    def info_chip(text: str, icon_name: str, color: str = colors.BLUE_400) -> Container:
        return Container(
            content=Row(
                controls=[
                    Icon(
                        name=icon_name,
                        size=14,
                        color=color,
                    ),
                    Text(
                        text,
                        size=12,
                        weight="w500",
                        color=colors.BLACK87,
                    ),
                ],
                spacing=4,
                alignment="center",
            ),
            padding=padding.symmetric(horizontal=8, vertical=4),
            bgcolor=colors.with_opacity(0.1, color),
            border_radius=15,
            height=28,
        )

    return Container(
        content=Column(
            controls=[
                Row(
                    controls=[
                        # Poster Container
                        # Container(
                        #     content=Image(
                        #         src=result.get("Poster", "https://via.placeholder.com/80x120?text=No+Poster"),
                        #         width=80,
                        #         height=120,
                        #         fit=ImageFit.COVER,
                        #         border_radius=8,
                        #     ) if result.get("Poster") and result.get("Poster") != "N/A" else None,
                        #     width=80,
                        #     visible=bool(result.get("Poster") and result.get("Poster") != "N/A")
                        # ),

                        # Main Content Column
                        Column(
                            expand=True,
                            spacing=8,
                            controls=[
                                # Title Row
                                Container(
                                    content=title_text,
                                    margin=margin.only(bottom=4),
                                ),
                                
                                # Info Chips Row in Scrollable Container
                                Container(
                                    content=Row(
                                        controls=[
                                            info_chip(result.get("Quality", "Unknown"), 
                                                    icons.HIGH_QUALITY_ROUNDED),
                                            info_chip(result.get("Size", "Unknown"), 
                                                    icons.DATA_USAGE_ROUNDED, 
                                                    colors.PURPLE_400),
                                            info_chip(f"{result.get('Seeds', '0')}/{result.get('Peers', '0')}", 
                                                    icons.GROUP_ROUNDED, 
                                                    colors.GREEN_400),
                                        ],
                                        spacing=8,
                                    ),
                                ),
                            ],
                        ),
                        
                        Row(
                            controls=[
                                IconButton(
                                    icon=icons.INFO_OUTLINE,
                                    icon_color=colors.BLUE_700,
                                    icon_size=24,
                                    tooltip="Show Details",
                                    on_click=lambda e, r=result: show_details(r),
                                ),
                                IconButton(
                                    icon=icons.DOWNLOAD_ROUNDED,
                                    icon_color=colors.WHITE,
                                    bgcolor=colors.GREEN_700,
                                    icon_size=24,
                                    tooltip="Download",
                                    on_click=lambda e, r=result: handle_download(r),
                                ),
                            ],
                            spacing=4,
                            alignment="center",
                        ),
                    ],
                    spacing=16,
                    alignment="start",
                ),
            ],
        ),
        gradient=LinearGradient(
            begin=alignment.center_left,
            end=alignment.center_right,
            colors=[
                colors.with_opacity(0.08, "#f8fafc"),  # Lighter, more subtle gradient
                colors.with_opacity(0.05, "#f8fafc"),
            ],
        ),
        animate=animation.Animation(200, AnimationCurve.EASE_OUT),
        padding=padding.all(12),
        bgcolor=colors.WHITE,
        border_radius=border_radius.all(10),
    )
