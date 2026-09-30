import requests
from PIL import Image
from io import BytesIO

def get_album_art(url, size):
    if url is None:
        return None
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.RequestException as e:
        print(f"Error fetching album art: {e}")
        return None

    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        img = img.resize((size, size), Image.Resampling.LANCZOS)
        img = img.convert('L').convert('RGB')
        noise = Image.effect_noise((size, size), 40)
        noise = noise.convert('RGB')
        img = Image.blend(img, noise, 0.30)
        return img
    else:
        print(f"Failed to fetch album art. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    from spotify_client import get_current_track
    track = get_current_track()
    if track:
        album_art_url = track['album_art']
        img = get_album_art(album_art_url, 300)
        if img:
            img.show()
    else:
        print("No track is currently playing.")


