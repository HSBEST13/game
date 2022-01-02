import pygame

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)


if __name__ == "__main__":
    sprites = pygame.sprite.Group()
    hero = pygame.sprite.Sprite(sprites)
    hero.image = pygame.image.load("data//images//hero//right.png")
    hero.rect = hero.image.get_rect()
    hero.rect.y = 500 - hero.image.get_rect()[3]
    hero.rect.x = 250
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            key_1 = pygame.key.get_pressed()
            key_2 = pygame.key.get_pressed()
            if key_1 == key_2:
                if key_1[pygame.K_UP]:
                    hero.rect.y -= 10
                if key_1[pygame.K_DOWN]:
                    hero.rect.y += 10
                if key_1[pygame.K_LEFT]:
                    hero.rect.x -= 10
                if key_1[pygame.K_RIGHT]:
                    hero.rect.x += 10
        screen.fill((0, 0, 0))
        sprites.draw(screen)
        sprites.update()
        pygame.display.flip()
    pygame.quit()
