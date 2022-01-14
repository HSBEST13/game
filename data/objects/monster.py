import pygame
import random
import ctypes


class Monster(pygame.sprite.Sprite):
    def __init__(self, *group):
        super(Monster, self).__init__(*group)
        self.image = pygame.image.load("data//images//hero//right.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(200, ctypes.windll.user32.GetSystemMetrics(0) - self.image.get_rect()[2])
        self.rect.y = ctypes.windll.user32.GetSystemMetrics(1) - self.image.get_rect()[3]
        self.uron = False

    def isuron(self):
        return self.uron

    def update(self, x, y):
        if x != self.rect.x:
            if x > self.rect.x:
                self.rect.x += 2
            else:
                self.rect.x -= 2
            self.uron = False
        else:
            self.uron = True
