import pygame
from data.classes.hero import Hero  # Класс с главным героем

pygame.init()
size = width, height = 1000, 600
screen = pygame.display.set_mode(size)


if __name__ == "__main__":
    sprites = pygame.sprite.Group()  # Группа спрайтов
    hero = Hero(sprites)
    running = True
    while running:
        if pygame.key.get_pressed()[pygame.K_LEFT]:  # Бег влево
            hero.left_()
        if pygame.key.get_pressed()[pygame.K_RIGHT]:  # Бег вправо
            hero.right_()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:  # Прыжок
                    hero.jump()
        screen.fill((0, 0, 0))
        sprites.draw(screen)
        sprites.update()
        pygame.display.flip()
    pygame.quit()
