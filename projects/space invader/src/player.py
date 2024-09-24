import pygame
from settings import settings
import bullet as bullet


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(settings.player_img)
        self.rect = self.image.get_rect(midtop=(settings.player_x_pos, settings.player_y_pos))
        self.live = settings.live

    def move_r(self):
        self.rect.x += settings.player_speed

    def move_l(self):
        self.rect.x -= settings.player_speed
