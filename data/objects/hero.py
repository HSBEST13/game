import pygame
import ctypes

hero_xp = 200


class Hero(pygame.sprite.Sprite):
    image = pygame.image.load("data//images//hero//right.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Hero.image
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = ctypes.windll.user32.GetSystemMetrics(1) - self.image.get_rect()[3]
        self.right_image = pygame.image.load("data//images//hero//right.png").convert_alpha()
        self.left_image = pygame.image.load("data//images//hero//left.png").convert_alpha()
        self.jump_flag = False  # Флаг и счетчик для прыжков
        self.jump_count = 200
        self.right = False  # Флаг для движения вправо
        self.left = False  # Флаг для движения влево
        self.collide_flag = False
        self.two = True
        self.flag = True

    def get_pos(self):
        return [self.rect.x, self.rect.y]

    def set_xp(self):
        global hero_xp
        hero_xp -= 1

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
                self.jump_count = 200
                self.jump_flag = False
            if 0 < self.jump_count <= 100:  # Если вдруг счетчик стал меньше или равен половине, то он падает
                self.rect.y += 5
            else:
                self.rect.y -= 5
            self.jump_count -= 5


class HealthBar(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.Surface((200, 20))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50

    def return_hp(self):
        global hero_xp
        return hero_xp

    def is_died(self):
        global hero_xp
        if hero_xp <= 0:
            return True

    def set_hp(self):
        global hero_xp
        hero_xp = 200


class Bullet(pygame.sprite.Sprite):
    def __init__(self, *group):
        super(Bullet, self).__init__(*group)
        self.image = pygame.Surface((20, 5))
        self.rect = self.image.get_rect()
        self.reverse = False

    def update(self):
        if self.reverse:
            self.rect.x -= 20
        else:
            self.rect.x += 20

    def set_pos(self, x, y, reverse):
        self.rect.x = x
        self.rect.y = y
        self.reverse = reverse
