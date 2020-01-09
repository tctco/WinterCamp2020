import time
from os import path
import pygame

WIDTH = 480
HEIGHT = 600
WHITE = (255,255,255)

pygame.mixer.pre_init(44100, -16, 1, 2048)
pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Piano Demo")
clock = pygame.time.Clock()

sound_dir = path.join(path.dirname(__file__), "sound")
print(sound_dir)
piano_sound_track_pack = []


def draw_text(text, font_size, surface, color, x, y):
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

def draw_UI():
    draw_text("Press a to z to play music", 20, screen, WHITE, WIDTH / 2, 100)
    draw_text("Press ESC to quit", 20, screen, WHITE, WIDTH / 2, 200)
    draw_text("Press space to play a piece automatically", 20, screen, WHITE, WIDTH / 2, 300)

def play_piece():
    with open("music_script.txt", "r") as f:
        for line in f.readlines():
            time.sleep(0.6)
            notes = line.split()
            for note in notes:
                piano_sound_track_pack[int(note) + 32].play()
                time.sleep(0.4)


for i in range(0, 68):
    piano_sound_track_pack.append(pygame.mixer.Sound(path.join(sound_dir, "note ({}).wav".format(i + 1))))

draw_UI()
pygame.display.flip()

while 1:
    clock.tick(100)
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            elif pygame.K_z >= event.key >= pygame.K_a:
                piano_sound_track_pack[event.key - ord('a') + 20].play()
            elif event.key == pygame.K_SPACE:
                pygame.event.set_blocked(pygame.KEYDOWN)
                play_piece()
                pygame.event.set_allowed(pygame.KEYDOWN)
