import pygame
from settings import settings


class CollisionManager:

    def __init__(self, player_group, enemy_group, player_bullets_group, alien_bullets_group, score_changer):
        self.player_group = player_group
        self.enemy_group = enemy_group
        self.player_bullets_group = player_bullets_group
        self.alien_bullets_group = alien_bullets_group
        self.score_changer = score_changer

    def check_collisions(self):
        pygame.sprite.groupcollide(self.player_bullets_group, self.alien_bullets_group, True, True)

        collided_enemies = pygame.sprite.groupcollide(self.player_bullets_group, self.enemy_group, True, False)
        if collided_enemies:
            settings.smash_sound.play()
            self.score_changer(1)
            for enemy in collided_enemies.values():
                for e in enemy:
                    e.live -= 1
                    if e.live <= 0:
                        e.kill()

        player = self.player_group.sprite
        if pygame.sprite.spritecollide(player, self.alien_bullets_group, True):
            player.live -= 1
            settings.hit_sound.play()

        if pygame.sprite.spritecollide(player, self.enemy_group, True):
            player.live = 0
