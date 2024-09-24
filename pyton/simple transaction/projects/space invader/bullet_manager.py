import pygame

from bullet import PlayerBullet, AlienBullet
from alien import Alien
from player import Player

class BulletManager:
    def __init__(self):
        self.player_bullets = pygame.sprite.Group()
        self.alien_bullets = pygame.sprite.Group()

    def add_bullet(self, entity):
        if isinstance(entity, Player):
            bullet = PlayerBullet(entity.rect.midbottom)
            self.player_bullets.add(bullet)
        elif isinstance(entity, Alien):
            if len(self.alien_bullets) < 4:
                bullet = AlienBullet(entity.rect.midbottom)
                self.alien_bullets.add(bullet)
        return True

    def init(self):
        self.player_bullets.empty()
        self.alien_bullets.empty()

    def update(self):
        self.player_bullets.update()
        self.alien_bullets.update()

    def draw(self, surface):
        self.player_bullets.draw(surface)
        self.alien_bullets.draw(surface)


