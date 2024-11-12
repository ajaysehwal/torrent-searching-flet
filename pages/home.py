import os
import json
import aiohttp
import asyncio
from datetime import datetime
from flet import *
import flet as ft
from components import MovieDetails, SearchCard, navbar, hero
from helpers import get_movie_details, search_movies
from components.skeltons import searchResults
from utils.speaktotext import SpeechToText
OMDB_API_URL = "http://www.omdbapi.com/"
OMDB_API_KEY = "494e9276"

class TorrentSearching:
    def __init__(self):
        self.page = None
        self.is_searching = False
        self.current_movie = None
        self.favorites = self.load_favorites()
        self.skeleton = searchResults.search_result_card_skeleton()
        self.loading= ListView(
            expand=True,
            spacing=20,
            padding=padding.only(left=20, right=20, top=30, bottom=30),
            animate_size=animation.Animation(300, "easeOutCubic"),
            visible=False,
        )
        
        
    def load_favorites(self):
        """Load favorites from file."""
        if os.path.exists("favorites.json"):
            try:
                with open("favorites.json", "r") as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading favorites: {e}")
        return {}
        
    def save_favorites(self):
        """Save favorites to file."""
        with open("favorites.json", "w") as f:
            json.dump(self.favorites, f)

    def main(self, page: ft.Page):
        self.page = page
        self.page.title = "TorrentFlix"
        self.setup_page_style()
        self.setup_layout()
        self.page.add(self.content_area)

    def setup_page_style(self):
        """Define the page style and fonts."""
        self.page.padding = 0
        self.page.spacing = 0
        self.page.fonts = {
            "Inter": "https://raw.githubusercontent.com/google/fonts/main/ofl/inter/Inter-Regular.ttf",
            "Poppins": "https://raw.githubusercontent.com/google/fonts/main/ofl/poppins/Poppins-Medium.ttf"
        }

    def setup_layout(self):
        """Set up the layout and components on the page."""
        self.navbar = navbar.create_navbar(self.page)
        self.search_box = self.create_search_box()
        self.welcome_text = hero.create_hero_section()
        self.results = self.create_results()
        self.favorites_grid = self.create_favorites_grid()
        
        self.content_area = Container(
            content=Column(
                controls=[
                    self.navbar,
                    self.welcome_text,
                    self.create_search_container(),
                    self.loading,
                    self.results,
                    self.favorites_grid,
                ],
                horizontal_alignment="center",
                spacing=0,
            ),
            expand=True,
        )
        self.movie_details = self.create_movie_details_dialog()
    def close_anchor(self,e):
        text = f"Color {e.control.data}"
        print(f"closing view from {text}")
        self.search_box.close_view(text)
    def handle_tap(self,e):
        print("handle_tap")
        self.search_box.open_view()
    def create_search_box(self):
        """Create the search box for movie search."""
        return SearchBar(
            view_elevation=1,
            height=55,
            expand=True,
            view_hint_text="suggestion",
            bar_bgcolor=colors.GREY_300,
            bar_hint_text="Search for content...",
            autofocus=True,
            on_tap=self.handle_tap,
            on_submit=self.handle_search,
            bar_trailing=[IconButton(icon=icons.MIC, tooltip="Voice Search",on_click=self.startlistening_sync), IconButton(icon=icons.SEARCH, on_click=self.handle_search)],
            controls=[
                ListTile(title=Text(f"india"), on_click=self.close_anchor, data=i,bgcolor=colors.GREY_300)
                for i in range(5)
            ],
        )
    def startlistening_sync(self, event=None):
       asyncio.run(self.startlistening(event))

    async def startlistening(self,event=None):
        speech_to_text = SpeechToText(noise_duration=1)
        result=speech_to_text.listen_and_recognize()
        if result:
          self.search_box.value=result
          await self.handle_search(None)
          self.page.update()
        
    def create_search_container(self):
        """Wrap the search box in a container with styling."""
        return Container(
            content=Row(controls=[self.search_box], alignment=MainAxisAlignment.CENTER, expand=True),
            padding=10
        )

    def create_results(self):
        """Create a grid to display search results."""
        return ListView(
            expand=True,
            spacing=20,
            padding=padding.only(left=20, right=20, top=30, bottom=30),
            animate_size=animation.Animation(300, "easeOutCubic"),
            visible=False,
        )

    def create_favorites_grid(self):
        """Create a grid to display favorite movies."""
        return GridView(
            expand=True,
            runs_count=5,
            max_extent=200,
            spacing=20,
            run_spacing=20,
            padding=20,
            visible=False,
        )

    def create_movie_details_dialog(self):
        """Create a dialog to show detailed movie information."""
        return AlertDialog(
            modal=True,
            bgcolor="#1e293b",
            content=Container(),
            actions=[
                OutlinedButton("Close", on_click=self.close_details),
                ElevatedButton("Add to Watchlist", on_click=self.add_to_favorites, style=ButtonStyle(color="white", bgcolor={"": "#3b82f6"})),
            ],
            actions_alignment="end",
            title_padding=padding.all(20),
            content_padding=padding.all(20),
            actions_padding=padding.all(20),
        )
    def handle_download(self,r):
       print("click for download")
    async def handle_search(self, e):
        """Handle search submit and display skeletons for 1 second before loading actual results."""
        query = self.search_box.value
        if not query:
            return
        self.search_box.close_view(query)

        self.results.controls.clear()
        self.loading.visible=True
        self.content_area.visible = True
        self.welcome_text.visible=False

        # Display skeleton loading cards
        for _ in range(6):
            self.loading.controls.append(self.skeleton)
        self.page.update()

        # Wait for 1 second to simulate loading
        await asyncio.sleep(2)
        self.loading.visible=False
        self.results.visible = True

        self.page.update()


        results = await search_movies(query)

        # Append search results
        for i, movie in enumerate(results):
            result_card = SearchCard.create_search_result_card(movie, self.show_movie_details, self.handle_download, self.page)
            self.results.controls.append(result_card)
            if i % 5 == 0:
                self.page.update()

        self.page.update()

    def show_movie_details(self, movie):
        """Show detailed movie information in a dialog."""
        self.current_movie = movie
        
        details = asyncio.run(get_movie_details(movie.get("imdbID")))
        if details:
            self.movie_details.content = MovieDetails.create_movie_details_content(details)
            self.movie_details.title = Text(details.get("Title", "Movie Details"))
        
        self.movie_details.open = True
        self.page.dialog = self.movie_details
        self.page.update()

    def close_details(self, e):
        """Close the movie details dialog."""
        self.movie_details.open = False
        self.current_movie = None
        self.page.update()

    def add_to_favorites(self, e):
        """Add the current movie to favorites."""
        if self.current_movie:
            movie_id = self.current_movie.get("imdbID")
            if movie_id:
                self.favorites[movie_id] = {
                    "movie": self.current_movie,
                    "added_date": datetime.now().isoformat(),
                }
                self.save_favorites()
                self.show_snack_bar("Added to favorites!")
                if self.favorites_grid.visible:
                    self.load_favorites_grid()
                self.update_favorite_button_in_dialog()

    def show_snack_bar(self, message: str):
        """Show a snack bar message."""
        self.page.show_snack_bar(SnackBar(content=Text(message), action="OK", action_color="primary"))

def home_page():
    return TorrentSearching()
