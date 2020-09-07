import pygame

from setting import Settings
from Ship import Ship
import game_functions as gf


def run_game():
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    while True:
        gf.check_events()

        screen.fill(ai_settings.bg_color)

        gf.update_screen(ai_settings, screen, ship)

run_game()
