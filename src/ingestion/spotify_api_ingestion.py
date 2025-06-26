import os
import json
import datetime
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Load credentials
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# Initialize Spotify API client
sp = Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
))

# Spotify Playlist ID (Today’s Top Hits)
PLAYLIST_ID = "37vVbInEzfnXJQjVuU7bAZ"

def fetch_top_50():
    try:
        response = sp.playlist_items(PLAYLIST_ID, market="US")
    except Exception as e:
        print(f"❌ Failed to fetch playlist: {e}")
        return

    today = datetime.date.today().isoformat()
    output_path = f"data/raw/top50_{today}.json"

    os.makedirs("data/raw", exist_ok=True)
    with open(output_path, "w") as f:
        for item in response['items']:
            track = item['track']
            if track is None:  # Defensive check
                continue
            record = {
                "track_name": track['name'],
                "artist": track['artists'][0]['name'],
                "album": track['album']['name'],
                "release_date": track['album']['release_date'],
                "popularity": track['popularity'],
                "duration_ms": track['duration_ms'],
                "explicit": track['explicit'],
                "date_fetched": today
            }
            f.write(json.dumps(record) + "\n")

if __name__ == "__main__":
    fetch_top_50()
