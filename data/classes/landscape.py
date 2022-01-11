import pygame
import ctypes
import pymunk.pygame_util

blocks = pygame.sprite.Group()


x = 0
y = 0


class StaticBlock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(blocks)
        self.image = pygame.Surface((80, 20))
        self.image.fill((77, 34, 14))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


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
        self.image.fill((196, 172, 147, 60))
        self.rect = self.image.get_rect()

    def set_pos(self, x_, y_, left, right):
        if left:
            self.rect.x = x_ - 80
        if right:
            self.rect.x = x_ + 220
        self.rect.y = y_ + 200

    def get_pos(self):
        return [self.rect.x, self.rect.y]

    def set_block(self):
        global x, y
        x = self.rect.x
        y = self.rect.y
        StaticBlock()


def create_square(space, pos):
    square_mass, square_size = 1, (60, 60)
    square_moment = pymunk.moment_for_box(square_mass, square_size)
    square_body = pymunk.Body(square_mass, square_moment)
    square_body.position = pos
    square_shape = pymunk.Poly.create_box(square_body, square_size)
    square_shape.elasticity = 0.4
    square_shape.friction = 1.0
    square_shape.color = (77, 34, 14, 255)
    space.add(square_body, square_shape)
