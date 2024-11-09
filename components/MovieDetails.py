from flet import Column,Row,Image,ImageFit,Text,Container,ScrollMode
def create_movie_details_content(movie) -> Column:
        """Create content for movie details dialog"""
        return Column(
            controls=[
                Row(
                    controls=[
                        Image(
                            src=movie.get("Poster", "N/A"),
                            width=200,
                            height=300,
                            fit=ImageFit.CONTAIN,
                            border_radius=10,
                        ),
                        Column(
                            controls=[
                                Text(
                                    movie.get("Title", "Unknown"),
                                    size=24,
                                    weight="bold",
                                    color="white",
                                ),
                                Text(
                                    f"{movie.get('Year', 'N/A')} • {movie.get('Runtime', 'N/A')}",
                                    size=16,
                                    color="#94a3b8",
                                ),
                                Container(height=10),
                                Text(
                                    f"Rating: {movie.get('imdbRating', 'N/A')} ⭐",
                                    size=16,
                                    color="#94a3b8",
                                ),
                                Text(
                                    f"Genre: {movie.get('Genre', 'N/A')}",
                                    size=16,
                                    color="#94a3b8",
                                ),
                                Container(height=20),
                                Text(
                                    movie.get("Plot", "No plot available."),
                                    size=14,
                                    color="white",
                                ),
                            ],
                            spacing=5,
                            expand=True,
                        ),
                    ],
                    spacing=20,
                ),
            ],
            scroll=ScrollMode.AUTO,
            height=400,
        )

