import pygame


pygame.mixer.init()


class Settings:

    def __init__(self):

        # general settings
        self.name = '"Space Invaders"'
        self.ticks = 60
        self.font_size = 45
        self.screen_width = 1300
        self.screen_height = 680
        self.screen_dest = (0, 0)
        self.background_img = 'graphics/new_background.png'
        self.background_pos = -200
        self.background_change = 2
        self.game_over_sound = pygame.mixer.Sound('sounds/game over.mp3')
        self.success_sound = pygame.mixer.Sound('sounds/success.mp3')
        self.sum_levels = 1
        self.live_dest = (10, 655)
        self.score_dest = (1150, 655)
        self.level_dest = (550, 655)
        self.line_start_pos = (0, 653)
        self.line_end_pos = (1300, 653)
        self.line_width = 3
        self.won_dest = (550, 300)
        self.won_font_size = 80

        # player settings
        self.player_img = 'graphics/player_1.png'
        self.player_x_pos = 600
        self.player_y_pos = 550
        self.player_speed = 7
        self.live = 3
        self.hit_sound = pygame.mixer.Sound('sounds/hit.mp3')

        # bullet settings
        self.bullet_img = 'graphics/shoot_1.png'
        self.enemy_bullet_img = 'graphics/shoot_4.png'
        self.bullet_plyer_speed = 4
        self.bullet_alin_speed = 5

        self.stuck = 5
        self.shoot_sound = pygame.mixer.Sound('sounds/shoot.mp3')
        self.shoot_sound.set_volume(0.25)

        # enemy settings
        self.enemy_img = 'graphics/alien.png'
        self.enemy_x_pos = 100
        self.enemy_y_pos = 80
        self.enemy_speed = 3
        self.enemy_down = 30
        self.shoot_amount = 100
        self.direction = 1
        self.smash_sound = pygame.mixer.Sound('sounds/smash.mpeg')
        self.enemy_rows = 3
        self.enemy_columns = 9
        self.enemy_width = 70
        self.enemy_height = 80

        # level_up settings
        self.increase_enemy_speed = 3
        self.increase_enemy_down = 10
        self.new_group_pos = -200
        self.increase_shoot_amount = 5
        self.increase_player_speed = 1


settings = Settings()
