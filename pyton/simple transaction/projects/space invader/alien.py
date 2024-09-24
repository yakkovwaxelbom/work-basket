import pygame

from settings import settings


class Alien(pygame.sprite.Sprite):
    def __init__(self, direction):
        super().__init__()
        self.image = pygame.image.load(settings.enemy_img)
        self.rect = self.image.get_rect(midtop=(settings.enemy_x_pos, settings.enemy_y_pos))
        self.direction = direction
        self.live = 1

    def update(self, shift_down):
        if shift_down:
            self.rect.y += settings.enemy_down
            self.direction *= -1
        self.rect.x += settings.enemy_speed * self.direction
