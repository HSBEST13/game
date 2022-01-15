import pygame
import ctypes
import time
from data.objects.hero import Hero, HealthBar, Bullet  # Класс с главным героем
from data.objects.button import Button  # Класс с кнопками
from data.objects.dialog import DialogWindow, DialogButtonExit  # Классы с элементами для диалогового окна
from data.objects.landscape import Landscape  # Класс с ландшафтом и блоком
from data.objects.monster import Monster

pygame.init()
pygame.mixer.init()
size = width, height = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

if __name__ == "__main__":
    """Инициализация групп спрайтов"""
    sprites = pygame.sprite.Group()  # Группа спрайтов
    buttons = pygame.sprite.Group()  # Группа кнопок
    dialog_parts = pygame.sprite.Group()  # Диалоговое окно
    monsters = pygame.sprite.Group()  # Враги
    cursor_group = pygame.sprite.Group()  # Курсор
    shoots = pygame.sprite.Group()  # Пули

    """Спрайты"""
    hero = Hero(sprites)  # Спрайт главного героя
    bar = HealthBar(sprites)
    start_button = Button(buttons)
    start_button.set_parameters(image_url="data//images//buttons and windows//start.png",  # Кнопка старта
                                hover_image_url="data//images//buttons and windows//start_hover.png",
                                x=ctypes.windll.user32.GetSystemMetrics(0) // 2 - 300,
                                y=ctypes.windll.user32.GetSystemMetrics(1) // 2 - 100)
    multiplayer_btn = Button()
    multiplayer_btn.set_parameters(image_url="data//images//buttons and windows//mp.png",
                                   hover_image_url="data//images//buttons and windows//mp_hover.png",
                                   x=ctypes.windll.user32.GetSystemMetrics(0) // 2 - 300,
                                   y=ctypes.windll.user32.GetSystemMetrics(1) // 2 - 100)
    singleplayer_btn = Button()
    singleplayer_btn.set_parameters(image_url="data//images//buttons and windows//sp.png",
                                    hover_image_url="data//images//buttons and windows//sp_hover.png",
                                    x=ctypes.windll.user32.GetSystemMetrics(0) // 2 - 300,
                                    y=ctypes.windll.user32.GetSystemMetrics(1) // 2 + 50)

    pygame.mouse.set_visible(False)
    cursor = pygame.sprite.Sprite(cursor_group)  # Спрайт мыши
    cursor.image = pygame.image.load("data//images//buttons and windows//cursor.png")
    cursor.rect = cursor.image.get_rect()

    land = Landscape(sprites)  # Спрайт, отвечающий за землю
    background_image = pygame.image.load("data/images/buttons and windows/background.gif")  # Картинка на фоне игры
    background_image = pygame.transform.scale(background_image, (ctypes.windll.user32.GetSystemMetrics(0),
                                                                 ctypes.windll.user32.GetSystemMetrics(1)))

    # Настройка и создание диалогового окна из частей
    dialog_window = DialogWindow(dialog_parts)  # Диалоговое окно
    dialog_window.set_parameters(x=ctypes.windll.user32.GetSystemMetrics(0) // 2 - 100,
                                 y=ctypes.windll.user32.GetSystemMetrics(1) // 2 - 200,
                                 width=200, height=400,
                                 background_color=(100, 102, 100))

    dialog_btn = DialogButtonExit(dialog_parts)  # Кнопка выхода из диалогового окна
    dialog_btn.set_pos(x=ctypes.windll.user32.GetSystemMetrics(0) // 2 + 70,
                       y=ctypes.windll.user32.GetSystemMetrics(1) // 2 - 200)

    """Инициализация музыки"""
    main_music = pygame.mixer.Sound("data//music//main_window.wav")  # Музыка диалоговых окон и главного меню
    shoot_music = pygame.mixer.Sound("data//music//shoot.wav")  # Звук выстрела
    game_music = pygame.mixer.Sound("data//music//game_music.wav")  # Музыка игры на фоне
    main_music.play(-1)  # Запуск главной музыки

    """Игра"""
    fps = 60
    clock = pygame.time.Clock()
    running = True
    start_window = True
    start_window_2 = False
    multiplayer = False
    singleplayer = False
    start_time = time.time()
    while running:  # Цикл игры
        if pygame.key.get_pressed()[pygame.K_a]:  # Бег влево
            hero.left_()
        if pygame.key.get_pressed()[pygame.K_d]:  # Бег вправо
            hero.right_()
        if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_SPACE]:  # Прыжок
            hero.jump()
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:  # Если игрок esc нажал, то заходит в меню
            dialog_btn.set_flag()
        if pygame.sprite.spritecollide(hero, land.blocks_to_return(), False):
            hero.collide()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not start_window and start_window_2:
                    shoot_music.play()
                    if hero.image == hero.right_image:
                        h = Bullet(shoots)
                        h.set_pos(hero.rect.x + 150, hero.rect.y + 150, False)
                    else:
                        h = Bullet(shoots)
                        h.set_pos(hero.rect.x + 50, hero.rect.y + 150, True)
                    for monster in monsters:
                        if pygame.sprite.spritecollide(monster, shoots, False):
                            monster.set_xp()
                    dialog_btn.check_click(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                if start_button.image == start_button.hover_image:
                    start_window_2 = True
                if singleplayer_btn.image == singleplayer_btn.hover_image and start_window:
                    singleplayer = True
                    start_window = False
                    monsters.empty()
                    main_music.stop()
                    game_music.play()
                    buttons.empty()
                if multiplayer_btn.image == multiplayer_btn.hover_image and start_window:
                    multiplayer = True
                    start_window = False
                    monsters.empty()
                    main_music.stop()
                    game_music.play()
                    buttons.empty()
            if event.type == pygame.MOUSEMOTION:
                cursor.rect.x = pygame.mouse.get_pos()[0]
                cursor.rect.y = pygame.mouse.get_pos()[1]
        blocks = land.blocks_to_return()
        screen.fill((0, 0, 0))
        screen.blit(background_image, (0, 0))
        if start_window:  # Обновление всего
            buttons.draw(screen)
            buttons.update(pygame.event.get())
            if start_window_2:
                buttons.empty()
                multiplayer_btn.add(buttons)
                singleplayer_btn.add(buttons)
                start_window_2 = False
        else:
            if singleplayer:
                dialog_parts.draw(screen)
                blocks.update()
                monsters.draw(screen)
                monsters.update(hero.rect.x, hero.rect.y)
                dialog_parts.update()
                sprites.draw(screen)
                sprites.update()
                shoots.draw(screen)
                shoots.update()
                if bar.is_died():
                    buttons.add(start_button)
                    start_window_2 = False
                    start_window = True
                    singleplayer = False
                    singleplayer_btn.image = singleplayer_btn.smart_image
                    bar.set_hp()
                if pygame.sprite.spritecollide(hero, monsters, False):
                    hero.set_xp()
                if bar.return_hp() >= 0:
                    pygame.draw.rect(screen, (255, 0, 0), (50 + bar.return_hp(), 50, 200 - bar.return_hp(), 20))
                else:
                    pygame.draw.rect(screen, (255, 0, 0), (50, 50, 200, 20))
            else:
                pass  # TODO multiplayer
        cursor_group.draw(screen)
        cursor_group.update()
        clock.tick(fps)
        pygame.display.flip()
        if time.time() - start_time >= 10:
            k = Monster(monsters)
            start_time = time.time()
    pygame.quit()
