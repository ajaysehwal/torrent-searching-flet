from typing import Dict, List, Optional
from dataclasses import dataclass, asdict

@dataclass
class Movie:
    """Data class for movie information"""
    imdb_id: str
    title: str
    year: str
    poster: str
    plot: Optional[str] = None
    rating: Optional[str] = None
    genre: Optional[str] = None
    runtime: Optional[str] = None
    director: Optional[str] = None
    size: Optional[str] = None
    seeds: Optional[int] = 0
    peers: Optional[int] = 0
    quality: Optional[str] = "1080p"  # Default quality

    @classmethod
    def from_api_response(cls, data: dict) -> 'Movie':
        return cls(
            imdb_id=data.get("imdbID", ""),
            title=data.get("Title", "Unknown"),
            year=data.get("Year", "N/A"),
            poster=data.get("Poster", ""),
            plot=data.get("Plot"),
            rating=data.get("imdbRating"),
            genre=data.get("Genre"),
            runtime=data.get("Runtime"),
            director=data.get("Director"),
            size="2.1 GB",  # Example size, replace with actual data
            seeds=1250,     # Example seeds, replace with actual data
            peers=100       # Example peers, replace with actual data
        )
