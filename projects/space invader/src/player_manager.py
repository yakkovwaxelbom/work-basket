import pygame
from settings import settings
from player import Player
from bullet import Bullet


class PlayerManager:

    def __init__(self, add_shot):

        self.player_group = pygame.sprite.GroupSingle()

        self.player_group.add(Player())

        self.last_shot_time = 0

        self.score = 0

        self.add_shot = add_shot

    def init(self):
        self.player_group.empty()
        self.player_group.add(Player())
        self.last_shot_time = 0
        self.score = 0

    def draw(self, surface):
        self.player_group.draw(surface)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move_left()
        if keys[pygame.K_RIGHT]:
            self.move_right()
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move_left(self):
        player = self.player_group.sprite
        if player.rect.left > 0:
            player.move_l()

    def move_right(self):
        player = self.player_group.sprite
        if player.rect.right < settings.screen_width:
            player.move_r()

    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time > 450:
            player = self.player_group.sprite
            was_shot = self.add_shot(player)
            if was_shot:
                self.last_shot_time = current_time

    def live(self):
        player = self.player_group.sprite
        return player.live
