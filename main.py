import pygame

pygame.init()
size = width, height = 1000, 600
screen = pygame.display.set_mode(size)


if __name__ == "__main__":
    jump_flag = False
    jump_count = 40
    sprites = pygame.sprite.Group()
    hero = pygame.sprite.Sprite(sprites)
    hero.image = pygame.image.load("data//images//hero//right.png")
    hero.rect = hero.image.get_rect()
    hero.rect.x = 250
    hero.rect.y = 600 - hero.image.get_rect()[3]
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    jump_flag = True
                    hero.rect.y -= 1
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            hero.image = pygame.image.load("data//images//hero//left.png")
            hero.rect.y = 600 - hero.image.get_rect()[3]
            hero.rect.x -= 1
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            hero.image = pygame.image.load("data//images//hero//right.png")
            hero.rect.y = 600 - hero.image.get_rect()[3]
            hero.rect.x += 1
        screen.fill((0, 0, 0))
        if jump_flag:
            if jump_count == 0:
                jump_count = 40
                jump_flag = False
                continue
            if jump_count <= 20:
                hero.rect.y += 1
            else:
                hero.rect.y -= 1
            jump_count -= 1
        sprites.draw(screen)
        sprites.update()
        pygame.display.flip()
    pygame.quit()
