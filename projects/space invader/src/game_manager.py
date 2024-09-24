import pygame

from collision_manager import CollisionManager
from state_manager import StateManager
from settings import settings
from bullet_manager import BulletManager
from player_manager import PlayerManager
from aliens_manager import EnemyManager
from ui_manager import UIManager


class GameManager:
    def __init__(self):
        self.screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

        self.game_state = 'start'
        self.state_manager = StateManager(self)
        self.level = 1

        self.bullet_manager = BulletManager()
        self.player_manager = PlayerManager(self.bullet_manager.add_bullet)
        self.enemy_manager = EnemyManager(self.bullet_manager.add_bullet)

        self.collisionManager = CollisionManager(self.player_manager.player_group, self.enemy_manager.enemy_group,
                                                 self.bullet_manager.player_bullets, self.bullet_manager.alien_bullets,
                                                 self.score_changer)

        self.ui_manager = UIManager(self.screen, self.changes_status)

    def changes_status(self, new_status):
        self.game_state = new_status

    def play(self):
        self.bullet_manager.update()
        self.player_manager.update()
        self.enemy_manager.update()

        self.bullet_manager.draw(self.screen)
        self.player_manager.draw(self.screen)
        self.enemy_manager.draw(self.screen)

        self.collisionManager.check_collisions()
        self.check_game_state()

        self.ui_manager.status_play(self.player_manager.live(), self.player_manager.score, self.level)

    def check_game_state(self):
        if self.player_manager.live() <= 0:
            self.game_state = 'game_over'
        elif len(self.enemy_manager.enemy_group) == 0:
            if self.level == settings.sum_levels:
                self.game_state = 'vin'
            else:
                self.level += 1
                self.game_state = 'between_levels'

    def init_game(self):
        self.level = 1
        self.player_manager.init()
        self.enemy_manager.init()
        self.bullet_manager.init()
        self.game_state = "playing"

    def start(self):

        self.ui_manager.display_start_screen()

    def vin(self):
        self.ui_manager.display_vin(self.player_manager.score)

    def game_over(self):
        self.ui_manager.display_game_over(self.player_manager.score)

    def between_levels(self):
        self.ui_manager.display_between_levels()

    def update(self):
        self.ui_manager.display_background()
        self.state_manager.run()
        pygame.display.update()

    def score_changer(self, value):
        self.player_manager.score += value
