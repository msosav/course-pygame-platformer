import pygame


class PhysicsEntity:
    """
    PhysicsEntity class represents an entity in the game with physical properties such as position, size, and velocity.

    Attributes:
        game (object): The game instance to which this entity belongs.
        type (str): The type of the entity.
        position (list): The [x, y] position of the entity.
        size (tuple): The (width, height) size of the entity.
        velocity (list): The [x, y] velocity of the entity.

    Methods:
        __init__(game, type, position, size):
            Initializes a new instance of PhysicsEntity.

        update(movement=(0, 0)) -> None:

        render(screen: pygame.Surface) -> None
    """

    def __init__(self, game: object, type: str, position: list, size: tuple) -> None:
        self.game = game
        self.type = type
        self.position = list(position)
        self.size = size
        self.velocity = [0, 0]

    def update(self, movement=(0, 0)) -> None:
        """
        Update the entity's position based on the given movement and its current velocity.

        Args:
            movement (tuple): A tuple containing the x and y movement values. Defaults to (0, 0).

        Returns:
            None
        """
        frame_movement = [
            movement[0] + self.velocity[0],
            movement[1] + self.velocity[1],
        ]

        self.position[0] += frame_movement[0]
        self.position[1] += frame_movement[1]

        self.velocity[1] += min(5, self.velocity[1] + 0.1)

    def render(self, surface: pygame.Surface) -> None:
        """
        Renders the player entity on the given surface.

        Args:
            surface (pygame.Surface): The surface on which to render the player.
        """
        surface.blit(self.game.assets["player"], self.position)
