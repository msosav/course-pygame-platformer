import pygame




class Tilemap:
    def __init__(self, game: object, tile_size: int = 16) -> None:
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrip_tiles = []

        for i in range(10):
            self.tilemap[str(3 + i) + ";10"] = {
                "type": "grass",
                "variant": 1,
                "pos": (3 + i, 10),
            }
            self.tilemap["10;" + str(5 + i)] = {
                "type": "stone",
                "variant": 1,
                "pos": (10, 5 + i),
            }

    def render(self, surface: pygame.Surface) -> None:
        """
        Render the tilemap and off-grid tiles onto the given surface.

        Args:
            surface (pygame.Surface): The surface to render the tiles onto.
        """
        for tile in self.offgrip_tiles:
            surface.blit(
                self.game.assets[tile["type"]][tile["variant"]],
                (tile["pos"][0]),
            )
        for location in self.tilemap:
            tile = self.tilemap[location]
            surface.blit(
                self.game.assets[tile["type"]][tile["variant"]],
                (tile["pos"][0] * self.tile_size, tile["pos"][1] * self.tile_size),
            )
