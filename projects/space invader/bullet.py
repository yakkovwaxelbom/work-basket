import pygame
from settings import settings


class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, direction, bullet_image):
        super().__init__()
        self.direction = direction
        self.image = pygame.image.load(bullet_image)
        self.rect = self.image.get_rect(midbottom=position)
        settings.shoot_sound.play()


class PlayerBullet(Bullet):
    def __init__(self, position):
        super().__init__(position, -1, settings.bullet_img)

    def update(self):
        if self.rect.y > 0:
            self.rect.y += settings.bullet_plyer_speed * self.direction
        else:
            self.kill()


class AlienBullet(Bullet):
    def __init__(self, position):
        super().__init__(position, 1, settings.enemy_bullet_img)

    def update(self):
        if self.rect.y < settings.screen_height:
            self.rect.y += settings.bullet_alin_speed * self.direction
        else:
            self.kill()
