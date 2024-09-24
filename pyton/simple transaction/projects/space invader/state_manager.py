import pygame

from settings import settings


class StateManager:

    def __init__(self, game_manager):
        self.game_manager = game_manager


    def run(self):
        if self.game_manager.game_state == "init_game":
            self.init_game()

        elif self.game_manager.game_state == 'start':
            self.play_start()

        elif self.game_manager.game_state == 'playing':
            self.play_game()

        elif self.game_manager.game_state == 'between_levels':
            self.between_levels()

        elif self.game_manager.game_state == 'game_over':
            self.game_over()

        elif self.game_manager.game_state == 'vin':
            self.vin()

    def play_game(self):
        self.game_manager.play()

    def play_start(self):
        self.game_manager.start()

    def vin(self):
        self.game_manager.vin()

    def game_over(self):
        self.game_manager.game_over()

    def init_game(self):
        self.game_manager.init_game()

    def between_levels(self):
        self.game_manager.between_levels()
