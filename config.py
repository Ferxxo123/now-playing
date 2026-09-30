# Configuration file for Spotify API credentials and polling interval

from dotenv import load_dotenv
import os   

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI") 

POLLING_INTERVAL = 3  # Interval in seconds to poll for currently playing track

REVEAL_TIME = 0.7

IDLE_TIME = 300

FULL_SCREEN = False

if not SPOTIFY_CLIENT_ID or not SPOTIFY_CLIENT_SECRET or not SPOTIFY_REDIRECT_URI:
    raise ValueError("Please set SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, and SPOTIFY_REDIRECT_URI in your .env file.")

