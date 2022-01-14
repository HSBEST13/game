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
        self.hero_x = 0
        self.hero_y = 0

    def set_hero_pos(self, x, y):
        self.hero_x = x
        self.hero_y = y

    def update(self):
        if self.hero_x != self.rect.x:
            if self.hero_x > self.rect.x:
                self.rect.x += 1
            else:
                self.rect.x -= 1
        else:
            print("boom")
