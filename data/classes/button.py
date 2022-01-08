import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self,  *group):
        super().__init__(*group)

    def set_parameters(self, x, y, width, height, text="", smart_color=(0, 0, 0),
                       hover_color=(0, 0, 0)):  # Установка параметров вне иницилизации
        self.text = text
        self.smart_image = pygame.Surface((width, height))
        self.smart_image.fill(smart_color)
        self.hover_image = pygame.Surface((width, height))
        self.hover_image.fill(hover_color)
        self.rect = self.smart_image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image = self.smart_image

    def update(self, events):
        self.image = self.smart_image
        if self.rect.collidepoint(pygame.mouse.get_pos()):  # Смена цвета при наведении на кнопку
            self.image = self.hover_image
