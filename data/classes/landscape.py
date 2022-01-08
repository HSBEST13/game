import pygame
import ctypes


class Landscape(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.Surface((ctypes.windll.user32.GetSystemMetrics(0), 20))
        self.image.fill((77, 34, 14))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = ctypes.windll.user32.GetSystemMetrics(1) - 20

    def update(self):
        pass
