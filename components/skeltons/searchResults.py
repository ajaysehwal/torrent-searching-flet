from flet import *

def search_result_card_skeleton() -> Container:
    """Create a skeleton version of the search result card with loading indicators."""
    
    def placeholder_chip(width: int, color: str = colors.GREY_300) -> Container:
        return Container(
            width=width,
            height=12,
            bgcolor=color,
            border_radius=8,
        )
    
    return Container(
        content=Column(
            controls=[
                Row(
                    controls=[
                        Column(
                            expand=True,
                            spacing=8,
                            controls=[
                                # Title Placeholder
                                Container(
                                    width=150,
                                    height=18,
                                    bgcolor=colors.GREY_300,
                                    border_radius=8,
                                    margin=margin.only(bottom=4),
                                ),
                                
                                # Info Chips Row Placeholder
                                Row(
                                    controls=[
                                        placeholder_chip(50),
                                        placeholder_chip(60),
                                        placeholder_chip(70),
                                    ],
                                    spacing=8,
                                ),
                            ],
                        ),
                        
                        Row(
                            controls=[
                                Container(
                                    width=32,
                                    height=32,
                                    bgcolor=colors.GREY_300,
                                    border_radius=12,
                                ),
                                Container(
                                    width=32,
                                    height=32,
                                    bgcolor=colors.GREY_300,
                                    border_radius=12,
                                    margin=margin.only(top=8),
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
                colors.with_opacity(0.08, "#f8fafc"),  # Light gradient for background effect
                colors.with_opacity(0.05, "#f8fafc"),
            ],
        ),
        padding=padding.all(12),
        bgcolor=colors.WHITE,
        border_radius=border_radius.all(10),
    )

