import pygame
from pygame.sprite import Group
from setting import Settings
from Ship import Ship
from Alien import Alien
from game_stats import GameStats
import game_functions as gf
from button import Button
from scoreboard import Scoreboard


def run_game():
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    screen.fill(ai_settings.bg_color)
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, "Play")
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # 创建飞船
    ship = Ship(ai_settings, screen)

    # 创建用于存储子弹的编组
    bullets = Group()

    # 创建外星人编组
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, ship, aliens, bullets, stats, sb, play_button)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
