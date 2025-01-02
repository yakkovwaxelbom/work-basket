import pygame
from settings import settings


class UIManager:

    def __init__(self, screen, changes_status):
        self.screen = screen
        self.background = pygame.image.load(settings.background_img)
        self.background_pos = settings.background_pos
        self.changes_status = changes_status

        self.sound_play = False

    def pres_enter(self, status):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.sound_play = False
            self.changes_status(status)

    def display_start_screen(self):
        my_font = pygame.font.Font(None, settings.font_size)
        title = my_font.render("Press enter to Start", True, "white")
        self.screen.blit(title, (settings.screen_width // 2 - title.get_width() // 2, settings.screen_height // 2))
        self.pres_enter('playing')

    def display_between_levels(self):
        my_font = pygame.font.Font(None, settings.font_size)
        between_text = my_font.render(f"Level {settings.level} Complete! Press Space for next level", True, "white")
        self.screen.blit(between_text,
                         (settings.screen_width // 2 - between_text.get_width() // 2, settings.screen_height // 2))
        self.pres_enter('playing')

    def display_game_over(self, score):
        font = pygame.font.Font(None, 74)
        small_font = pygame.font.Font(None, 50)

        game_over_text = font.render("game over", True, (255, 0, 0))
        game_over_rect = game_over_text.get_rect(center=(settings.screen_width // 2, settings.screen_height // 3))
        self.screen.blit(game_over_text, game_over_rect)

        score_text = font.render(f"final score: {score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(settings.screen_width // 2, settings.screen_height // 2))
        self.screen.blit(score_text, score_rect)

        continue_text = small_font.render("Press Space to continue", True, (255, 255, 0))
        continue_rect = continue_text.get_rect(center=(settings.screen_width // 2, settings.screen_height // 1.5))
        self.screen.blit(continue_text, continue_rect)

        if not self.sound_play:
            settings.game_over_sound.play()
            self.sound_play = True

        self.pres_enter('init_game')

    def display_vin(self, score):
        font = pygame.font.Font(None, 74)
        small_font = pygame.font.Font(None, 50)

        game_over_text = font.render("your vin", True, (255, 0, 0))
        game_over_rect = game_over_text.get_rect(center=(settings.screen_width // 2, settings.screen_height // 3))
        self.screen.blit(game_over_text, game_over_rect)

        score_text = font.render(f"final score: {score}", True, (255, 255, 255))  # צבע לבן
        score_rect = score_text.get_rect(center=(settings.screen_width // 2, settings.screen_height // 2))
        self.screen.blit(score_text, score_rect)

        continue_text = small_font.render("Press Space to continue", True, (255, 255, 0))  # צבע צהוב
        continue_rect = continue_text.get_rect(center=(settings.screen_width // 2, settings.screen_height // 1.5))
        self.screen.blit(continue_text, continue_rect)

        settings.success_sound.play()

        self.pres_enter('init_game')

    def display_background(self):
        self.screen.blit(self.background, (0, self.background_pos))
        if self.background_pos < 0:
            self.background_pos += settings.background_change
        else:
            self.background_pos = settings.background_pos

    def status_play(self, live, score, level):
        my_font = pygame.font.Font(None, settings.font_size)
        live = my_font.render(f"Live = {live}", False, "yellow")
        score = my_font.render(f"Score = {score}", False, "green")
        level = my_font.render(f"Level {level}", False, "orange")
        self.screen.blit(live, settings.live_dest)
        self.screen.blit(score, settings.score_dest)
        self.screen.blit(level, settings.level_dest)
        pygame.draw.line(self.screen, "red", settings.line_start_pos, settings.line_end_pos,
                         settings.line_width)
