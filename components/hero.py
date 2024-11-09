from flet import Container,Column,Text,TextAlign,padding
def create_hero_section():
   return Container(
            content=Column(
                controls=[
                    Container(height=40),
                    Text(
                        "Discover Digital Content",
                        size=48,
                        weight="bold",
                        color="black",
                        font_family="Poppins",
                        text_align=TextAlign.CENTER,
                    ),
                    Container(height=10),
                    Text(
                        "Search through a vast library of digital resources. Find exactly what you're looking for.",
                        size=16,
                        color="#94a3b8",
                        font_family="Inter",
                        text_align=TextAlign.CENTER,
                    ),
                    Container(height=40),
                ],
                horizontal_alignment="center",
                spacing=0,
            ),
            padding=padding.symmetric(horizontal=20),
        )
