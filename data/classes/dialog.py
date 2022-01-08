import pygame

show_flag = True


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
        global show_flag
        if not show_flag:
            self.image = pygame.Surface((0, 0))
        else:
            self.image = self.field


class DialogButtonExit(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image_exit = pygame.image.load("data//images//buttons and windows//button_exit.png")
        self.image = self.image_exit
        self.hidden_img = pygame.Surface((0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 120
        self.rect.y = 50

    def check_click(self, x, y):
        global show_flag
        if self.rect.collidepoint(x, y):
            show_flag = False

    def update(self):
        global show_flag
        if not show_flag:
            self.image = self.hidden_img
            show_flag = False
        else:
            self.image = self.image_exit
            show_flag = True
