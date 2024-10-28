import os

import pygame

BASE_IMAGE_PATH = "data/images/"


def load_image(path: str) -> pygame.Surface:
    """
    Loads an image from the specified path, sets the color key to black (0, 0, 0), and returns the image surface.

    Args:
        path (str): The relative path to the image file.

    Returns:
        pygame.Surface: The loaded image with the color key set.
    """
    image = pygame.image.load(BASE_IMAGE_PATH + path)
    image.set_colorkey((0, 0, 0))

    return image


def load_images(path: str) -> list[pygame.Surface]:
    """
    Loads all images from the specified path and returns them as a list of image surfaces.

    Args:
        path (str): The relative path to the image files.

    Returns:
        list[pygame.Surface]: A list of loaded images with the color key set.
    """
    images = []

    for image_name in sorted(os.listdir(BASE_IMAGE_PATH + path)):
        images.append(load_image(path + "/" + image_name))

    return images
