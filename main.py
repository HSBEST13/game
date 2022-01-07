import pygame
from data.classes.hero import Hero

pygame.init()
size = width, height = 1000, 600
screen = pygame.display.set_mode(size)


if __name__ == "__main__":
    sprites = pygame.sprite.Group()
    hero = Hero(sprites)
    running = True
    while running:
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            hero.left_()
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            hero.right_()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    hero.jump()
        screen.fill((0, 0, 0))
        sprites.draw(screen)
        sprites.update()
        pygame.display.flip()
    pygame.quit()
