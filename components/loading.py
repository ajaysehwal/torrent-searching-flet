import flet as ft
def create_loading_indicator() -> ft.ProgressRing:
        return ft.ProgressRing(
            width=24,
            height=24,
            stroke_width=2,
            color="#3b82f6",
            visible=False
        )
    
