import pygame
from game_manager import GameManager


def main():
    pygame.init()
    game = GameManager()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        game.update()


if __name__ == '__main__':
    main()
