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

    def left_(self):
        self.right = False
        self.left = True

    def right_(self):
        self.right = True
        self.left = False

    def jump(self):
        self.jump_flag = True

    def set_visible(self, visible=True):
        self.visible = visible

    def update(self):
        if not self.visible:
            self.image = pygame.Surface((0, 0))
        else:
            self.image = self.right_image
        if self.right and self.visible:  # Если правая кнопка
            self.rect.x += 5
            self.image = self.right_image
            self.right = False
        if self.left and self.visible:  # Если левая кнопка
            self.image = self.left_image
            self.rect.x -= 5
            self.left = False
        if self.jump_flag and self.visible:  # Прыжок
            if self.jump_count == 0:
                self.jump_count = 200
                self.jump_flag = False
            if 0 < self.jump_count <= 100:  # Если вдруг счетчик стал меньше или равен половине, то он падает
                self.rect.y += 5
            else:
                self.rect.y -= 5
            self.jump_count -= 5
