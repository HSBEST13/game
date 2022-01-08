import pygame
from data.classes.hero import Hero  # Класс с главным героем
from data.classes.button import Button  # Класс с кнопками
from data.classes.dialog import DialogWindow, DialogButtonExit

pygame.init()
size = width, height = 1000, 600
screen = pygame.display.set_mode(size)

if __name__ == "__main__":
    sprites = pygame.sprite.Group()  # Группа спрайтов
    buttons = pygame.sprite.Group()  # Группа кнопок
    hero = Hero(sprites)
    dialog = DialogWindow(sprites)
    dialog.set_parameters(50, 50, 100, 200, (213, 4, 121))
    fps = 200
    clock = pygame.time.Clock()
    running = True
    while running:
        if pygame.key.get_pressed()[pygame.K_LEFT]:  # Бег влево
            hero.left_()
        if pygame.key.get_pressed()[pygame.K_RIGHT]:  # Бег вправо
            hero.right_()
        if pygame.key.get_pressed()[pygame.K_UP]:  # Прыжок
            hero.jump()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        sprites.draw(screen)
        sprites.update()
        buttons.draw(screen)
        buttons.update(pygame.event.get())
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
