import pygame


class DialogWindow(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)

    def set_parameters(self, x, y, width, height, background_color=(255, 255, 255)):
        self.field = pygame.Surface((width, height))
        self.field.fill(background_color)
        self.rect = self.field.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image = self.field

    def update(self):
        pass


class DialogButtonExit(pygame.sprite.Sprite):
    def __init__(self):
        self.image_exit = pygame.image.load("data//images//buttons and windows//")
