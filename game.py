import sys

import pygame

from scripts.entities import PhysicsEntity
from scripts.tilemap import Tilemap
from scripts.utils import load_image, load_images


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Ninja Game")
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))  # Half the size of the screen

        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        self.assets = {
            "decor": load_images("tiles/decor"),
            "grass": load_images("tiles/grass"),
            "stone": load_images("tiles/stone"),
            "large_decor": load_images("tiles/large_decor"),
            "player": load_image("entities/player.png"),
        }

        self.player = PhysicsEntity(self, "player", [50, 50], (8, 13))

        self.tilemap = Tilemap(self)

    def run(self):
        while True:
            self.display.fill((14, 219, 248))

            self.tilemap.render(self.display)

            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    elif event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    elif event.key == pygame.K_RIGHT:
                        self.movement[1] = False

            self.screen.blit(
                pygame.transform.scale(self.display, self.screen.get_size()), (0, 0)
            )
            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Game()
    game.run()
