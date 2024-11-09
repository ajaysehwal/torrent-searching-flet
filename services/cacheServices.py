import hashlib
import os
import json
from utils.logger import setup_logger
from typing import Optional

logger=setup_logger() 
CACHE_DIR = "cache"
FAVORITES_FILE = "favorites.json"

class CacheManager:
    """Handle caching of API responses"""
    def __init__(self, cache_dir: str = CACHE_DIR):
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)
    
    def _get_cache_key(self, query: str) -> str:
        return hashlib.md5(query.encode()).hexdigest()
    
    def get_cached_data(self, query: str) -> Optional[dict]:
        cache_key = self._get_cache_key(query)
        cache_file = os.path.join(self.cache_dir, f"{cache_key}.json")
        
        if os.path.exists(cache_file):
            try:
                with open(cache_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Cache read error: {e}")
        return None
    
    def cache_data(self, query: str, data: dict):
        cache_key = self._get_cache_key(query)
        cache_file = os.path.join(self.cache_dir, f"{cache_key}.json")
        
        try:
            with open(cache_file, 'w') as f:
                json.dump(data, f)
        except Exception as e:
            logger.error(f"Cache write error: {e}")
