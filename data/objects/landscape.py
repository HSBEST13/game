import pygame
import ctypes

blocks = pygame.sprite.Group()


x = 0
y = 0


class Landscape(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.Surface((ctypes.windll.user32.GetSystemMetrics(0), 20))
        self.image.fill((127, 48, 46))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = ctypes.windll.user32.GetSystemMetrics(1) - 20

    def blocks_to_return(self):
        global blocks
        return blocks


class Block(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.Surface((80, 20))
        self.rect = self.image.get_rect()

    def set_pos(self, x_, y_, left, right):
        if left:
            self.rect.x = x_ - 80
        if right:
            self.rect.x = x_ + 220
        self.rect.y = y_ + 200

    def get_pos(self):
        return [self.rect.x, self.rect.y]
