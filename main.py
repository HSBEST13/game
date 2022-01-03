import pygame

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)


if __name__ == "__main__":
    sprites = pygame.sprite.Group()
    hero = pygame.sprite.Sprite(sprites)
    hero.image = pygame.image.load("data//images//hero//right.png")
    hero.rect = hero.image.get_rect()
    hero.rect.x = 250
    hero.rect.y = 500 - hero.image.get_rect()[3]
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if pygame.key.get_pressed()[pygame.K_UP]:
            hero.rect.y -= 1
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            hero.rect.y += 1
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            hero.image = pygame.image.load("data//images//hero//left.png")
            hero.rect.y = 500 - hero.image.get_rect()[3]
            hero.rect.x -= 1
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            hero.image = pygame.image.load("data//images//hero//right.png")
            hero.rect.y = 500 - hero.image.get_rect()[3]
            hero.rect.x += 1
        screen.fill((0, 0, 0))
        sprites.draw(screen)
        sprites.update()
        pygame.display.flip()
    pygame.quit()
