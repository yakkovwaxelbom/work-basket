import pygame
import random

from alien import Alien

from settings import settings


class EnemyManager:

    def __init__(self, add_shot):
        self.enemy_group = pygame.sprite.Group()
        self.last_shoot_time = 0
        self.add_shot = add_shot
        self.init()

    def draw(self, surface):
        self.enemy_group.draw(surface)

    def update(self):
        shift_down = False
        for enemy in self.enemy_group.sprites():
            if enemy.rect.left <= 0 or enemy.rect.right >= settings.screen_width:
                shift_down = True
                break
        self.enemy_group.update(shift_down)
        self.shoot()

    def init(self):
        self.enemy_group.empty()
        y = settings.enemy_y_pos
        x_start = settings.screen_width - (settings.enemy_width * settings.enemy_columns)  # התחלה מהפינה הימנית
        for i in range(settings.enemy_rows):
            x = x_start
            for j in range(settings.enemy_columns):
                enemy = Alien(1)
                self.enemy_group.add(enemy)
                enemy.rect.left = x
                enemy.rect.bottom = y
                x += settings.enemy_width
            y += settings.enemy_height

    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shoot_time > 850 and len(self.enemy_group) > 0:
            random_enemy = random.choice(self.enemy_group.sprites())
            self.add_shot(random_enemy)
            self.last_shoot_time = current_time
