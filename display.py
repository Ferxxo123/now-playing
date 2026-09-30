import pygame
import time
from config import FULL_SCREEN

pygame.init()

if FULL_SCREEN:
    screen = pygame.display.set_mode((800, 480), pygame.FULLSCREEN )
    pygame.mouse.set_visible(False)
else:
    screen = pygame.display.set_mode((800, 480))
pygame.display.set_caption("Now Playing")

title_font = pygame.font.SysFont("courier new, courier, dejavusansmono", 40)
artist_font = pygame.font.SysFont("courier new, courier, dejavusansmono", 32)
time_font = pygame.font.SysFont("courier new, courier, dejavusansmono", 20)
clock_font = pygame.font.SysFont("courier new, courier, dejavusansmono", 120)

bar_x = 480
bar_y = 320
bar_width = 280
bar_height = 6


def make_cover(img):
    if img is None:
        return None
    return pygame.image.frombytes(img.tobytes(), img.size, img.mode)

def fit_text(text, font, max_width):
    if font.size(text)[0] <= max_width:
        return text

    while text and font.size(text + '...')[0] > max_width:
        text = text[:-1]
    return text.rstrip() + '...'

def format_time(seconds):
    seconds = int(seconds)
    minutes = seconds // 60
    secs = seconds % 60
    return f'{minutes}:{secs:02d}'

def draw_clock():
    screen.fill((20,20,20))
    clock_text = clock_font.render(time.strftime('%H:%M'), True, (255, 255, 255))
    x =  (800 - clock_text.get_width()) // 2
    y = (480 - clock_text.get_height()) // 2

    screen.blit(clock_text, (x, y))

    pygame.display.flip()

def draw(track, cover, reveal=1):
    screen.fill((20, 20, 20))  # Clear the screen with grey

    if cover is not None:
        visible = int(400 * reveal)
        visible = visible // 10 * 10
        screen.blit(cover, (40, 40), area=(0, 0, 400, visible))  # Draw the album cover

    title_text = title_font.render(fit_text(track['track_name'], title_font, bar_width), True, (255, 255, 255))
    artist_text = artist_font.render(fit_text(track['artist_name'], artist_font, bar_width), True, (180, 180, 180))
    
    screen.blit(title_text, (480, 180))  # Draw the song title
    screen.blit(artist_text, (480, 240))  # Draw the artist name

    pygame.draw.rect(screen, (100, 100, 100), (bar_x, bar_y, bar_width, bar_height))  # Draw the progress bar
    fraction = track['progress'] / track['duration'] if track['duration'] > 0 else 0
    filled_width = int(bar_width * fraction)

    pygame.draw.rect(screen, (255, 255, 255), (bar_x, bar_y, filled_width, bar_height))  # Draw the filled part of the progress bar

    elapsed_text = time_font.render(format_time(track['progress']), True, (180, 180, 180))
    total_text = time_font.render(format_time(track['duration']), True, (180, 180, 180))
    screen.blit(elapsed_text, (bar_x, bar_y + 14))

    right_x = bar_x + bar_width - total_text.get_width()
    screen.blit(total_text, (right_x, bar_y + 14))

    pygame.display.flip()  # Update the display




if __name__ == "__main__":
    from spotify_client import get_current_track
    from artwork import get_album_art

    clock = pygame.time.Clock()

    track = get_current_track()
    img = get_album_art(track['album_art'], 400)
    cover = make_cover(img)

    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False

        draw(track, cover)
        clock.tick(30)  # Limit to 30 frames per second

    pygame.quit()