import pygame
import random
import ctypes

monster_xp = 100


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

    def set_xp(self):
        global monster_xp
        monster_xp -= 10

    def update(self, x, y):
        global monster_xp
        if monster_xp == 0:
            self.image = pygame.Surface((0, 0))
            self.rect.y = 10000
        else:
            if x != self.rect.x:
                if x > self.rect.x:
                    self.rect.x += 2
                else:
                    self.rect.x -= 2
                self.uron = False
            else:
                self.uron = True
