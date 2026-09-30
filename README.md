# Now Playing 🎵

A vintage-style "now playing" screen for Spotify, built with Python and Pygame, designed to run on a Raspberry Pi with a small touchscreen.

It shows the song you're listening to on any device (phone, laptop, speaker) with a black-and-white album cover, film grain, a retro top-to-bottom loading animation, and a typewriter font. When no music is playing, it turns into a clock.

## Features

- Shows the current song, artist, and album cover from your Spotify account
- Black-and-white cover with film grain for a vintage look
- Retro loading animation when the song changes, like old dial-up images
- Smooth progress bar with elapsed and total time
- Long titles are shortened with "..." so they fit the screen
- Keeps showing the last song when paused
- Switches to a clock after a few minutes without music
- Survives internet drops without crashing
- Fullscreen mode for the Raspberry Pi

## Hardware

- Raspberry Pi 5 (or Pi 4) with power supply and microSD card
- 800×480 screen (e.g. a 7" DSI touchscreen)

It also runs on any computer in a normal window, which is handy for development.

## Setup

### 1. Create a Spotify app

1. Go to [developer.spotify.com](https://developer.spotify.com/dashboard) and create an app
2. Add `http://127.0.0.1:8888/callback` as a Redirect URI
3. Select **Web API**
4. Copy your **Client ID** and **Client Secret**

### 2. Add your keys

Copy `.env.example` to a new file called `.env` and fill in your keys:

```
SPOTIFY_CLIENT_ID=your_client_id_here
SPOTIFY_CLIENT_SECRET=your_client_secret_here
SPOTIFY_REDIRECT_URI=http://127.0.0.1:8888/callback
```

### 3. Install the libraries

```
pip install -r requirements.txt
```

### 4. Run it

Play a song on Spotify, then:

```
python main.py
```

The first time, a browser window opens so you can approve access to your Spotify account.

## Settings

All settings are in `config.py`:

| Setting | What it does |
| --- | --- |
| `POLLING_INTERVAL` | Seconds between checks for the current song |
| `REVEAL_TIME` | Seconds for the cover loading animation |
| `IDLE_TIME` | Seconds without music before showing the clock |
| `FULL_SCREEN` | `True` on the Raspberry Pi, `False` on your computer |

## Project structure

```
now-playing/
├── config.py          settings and keys
├── spotify_client.py  asks Spotify what's playing
├── artwork.py         downloads and styles the album cover
├── display.py         draws the song screen and the clock
├── main.py            the loop that connects everything
└── requirements.txt   libraries to install
```

## Built with

- [spotipy](https://spotipy.readthedocs.io/) for the Spotify Web API
- [Pygame](https://www.pygame.org/) for drawing on the screen
- [Pillow](https://python-pillow.org/) for image effects
