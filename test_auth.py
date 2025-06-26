from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv()

sp = Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")
))

results = sp.search(q='playlist', type='playlist', limit=5)
for idx, item in enumerate(results.get('playlists', {}).get('items', [])):
    if not item or 'name' not in item or 'id' not in item:
        continue
    print(f"{idx+1}. {item['name']} – {item['id']}")

