import spotipy
from spotipy.oauth2 import SpotifyOAuth 
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI
import requests

sp  =  spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                                client_secret=SPOTIFY_CLIENT_SECRET,
                                                redirect_uri=SPOTIFY_REDIRECT_URI,
                                                scope="user-read-currently-playing"))



def get_current_track():
    try:
        data = sp.current_user_playing_track()
    except (requests.RequestException, spotipy.SpotifyException) as e:
        print(f'Error in: {e}')
        return None
    
    if data is None or data['item'] is None:
        return None
    track_name = data['item']['name']
    artist_name = data['item']['artists'][0]['name']
    album_art = data['item']['album']['images'][0]['url']   
    progress = data['progress_ms'] / 1000  # Convert milliseconds to seconds
    duration = data['item']['duration_ms'] / 1000  # Convert milliseconds to seconds
    is_playing = data['is_playing']
    
    return {
        'track_name': track_name,
        'artist_name': artist_name,
        'album_art': album_art,
        'progress': progress,
        'duration': duration,
        'is_playing': is_playing
    }

if __name__ == "__main__":
    print(get_current_track())