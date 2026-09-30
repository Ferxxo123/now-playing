import time
import pygame

from config import POLLING_INTERVAL, IDLE_TIME, REVEAL_TIME
from spotify_client import get_current_track
from artwork import get_album_art
from display import draw, make_cover, draw_clock

clock = pygame.time.Clock()
current_track = None
cover = None
last_poll = 0
cover_time = 0
running = True
last_active = 0


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = time.time()
    if now - last_poll >= POLLING_INTERVAL:
        last_poll = now
        new_track = get_current_track()
       

        if new_track is not None:
            # Check if the track has changed
            if current_track is None or new_track['track_name'] != current_track['track_name']: #this line checks if the track has changed
                current_track = new_track
                img = get_album_art(current_track['album_art'], 400)
                cover = make_cover(img)
                cover_time = now

            current_track = new_track
            if new_track['is_playing']:
                last_active = now

    # Draw the current track and cover if available
    
    if current_track is None or now - last_active > IDLE_TIME:
        draw_clock()
    else:
        shown = dict(current_track) #this is a copy 
        if shown['is_playing']:
            shown['progress'] = min(now - last_poll + shown['progress'], shown['duration'])  # Update progress if playing
        reveal = min(1, (now-cover_time) / REVEAL_TIME )
        draw(shown, cover, reveal)
    clock.tick(30)  # Limit to 30 frames per second

pygame.quit()

