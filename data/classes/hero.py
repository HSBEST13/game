import pygame
import ctypes


class Hero(pygame.sprite.Sprite):
    image = pygame.image.load("data//images//hero//right.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Hero.image
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = ctypes.windll.user32.GetSystemMetrics(1) - self.image.get_rect()[3]
        self.right_image = pygame.image.load("data//images//hero//right.png")
        self.left_image = pygame.image.load("data//images//hero//left.png")
        self.jump_flag = False  # Флаг и счетчик для прыжков
        self.jump_count = 200
        self.right = False  # Флаг для движения вправо
        self.left = False  # Флаг для движения влево
        self.collide_flag = False
        self.two = True

    def left_(self):
        self.right = False
        self.left = True

    def right_(self):
        self.right = True
        self.left = False

    def collide(self):
        self.collide_flag = True

    def jump(self):
        self.jump_flag = True

    def update(self):
        if self.collide_flag and self.two:
            if self.rect.y != ctypes.windll.user32.GetSystemMetrics(1) - self.image.get_rect()[3]:
                self.jump_flag = False
                self.two = False
        if self.right:  # Если правая кнопка
            self.rect.x += 5
            self.image = self.right_image
            self.right = False
        if self.left:  # Если левая кнопка
            self.image = self.left_image
            self.rect.x -= 5
            self.left = False
        if self.jump_flag:  # Прыжок
            if self.jump_count == 0:
                self.jump_cowunt = 200
                self.jump_flag = False
            if 0 < self.jump_count <= 100:  # Если вдруг счетчик стал меньше или равен половине, то он падает
                self.rect.y += 5
            else:
                self.rect.y -= 5
            self.jump_count -= 5
