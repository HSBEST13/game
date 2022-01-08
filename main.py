import pygame
import ctypes
from data.classes.hero import Hero  # Класс с главным героем
from data.classes.button import Button  # Класс с кнопками
from data.classes.dialog import DialogWindow, DialogButtonExit  # Классы с элементами для диалогового окна

pygame.init()
pygame.mixer.init()
size = width, height = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

if __name__ == "__main__":
    sprites = pygame.sprite.Group()  # Группа спрайтов
    buttons = pygame.sprite.Group()  # Группа кнопок
    dialog_parts = pygame.sprite.Group()  # Диалоговое окно
    hero = Hero(sprites)  # Спрайт главного героя
    dialog_btn = DialogButtonExit(dialog_parts)
    dialog_btn.set_pos(120, 50)
    fps = 200
    clock = pygame.time.Clock()
    running = True
    main_music = pygame.mixer.Sound("data//music//main_window.wav")
    shoot_music = pygame.mixer.Sound("data//music//shoot.wav")
    main_music.play()
    while running:
        if pygame.key.get_pressed()[pygame.K_LEFT]:  # Бег влево
            hero.left_()
        if pygame.key.get_pressed()[pygame.K_RIGHT]:  # Бег вправо
            hero.right_()
        if pygame.key.get_pressed()[pygame.K_UP]:  # Прыжок
            hero.jump()
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:  # Если игрок esc нажал, то заходит в меню
            dialog_btn.set_flag()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                dialog_btn.check_click(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            if event.type == pygame.MOUSEBUTTONUP:

        screen.fill((0, 0, 0))
        sprites.draw(screen)  # Обновление всего
        sprites.update()
        buttons.draw(screen)
        buttons.update(pygame.event.get())
        dialog_parts.draw(screen)
        dialog_parts.update()
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
