import sys
import pygame


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Ninja Game')
        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()

        self.img = pygame.image.load('data/images/clouds/cloud_1.png')
        self.img.set_colorkey((0, 0, 0))

        self.img_pos = [160, 260]
        self.movements = [False, False]

        self.collision_area = pygame.Rect(50, 50, 300, 50)

    def run(self):
        while True:
            self.screen.fill((14, 219, 248))

            img_r = pygame.Rect(
                self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())

            if img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen, (0, 100, 255),
                                 self.collision_area)

            self.img_pos[1] += (self.movements[1] - self.movements[0]) * 5
            self.screen.blit(self.img, self.img_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movements[0] = True
                    elif event.key == pygame.K_DOWN:
                        self.movements[1] = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movements[0] = False
                    elif event.key == pygame.K_DOWN:
                        self.movements[1] = False

            pygame.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.run()
