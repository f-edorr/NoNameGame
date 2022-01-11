import pygame
from Img_Editor import ImgEditor

SIZE = WIDTH, HEIGHT = 700, 500

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('NoNameGame')
    monitor = [pygame.display.Info().current_w, pygame.display.Info().current_h]
    screen = pygame.display.set_mode(SIZE)
    editor = ImgEditor()
    pygame.display.set_icon(editor.load_image("icon.png"))
    fullscreen = False

    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()
    img = editor.load_image("menu.png", f"\main_menu")
    sprite.image = img
    sprite.rect = sprite.image.get_rect()

    sprite.rect.x = 0
    sprite.rect.y = 0
    all_sprites.add(sprite)

    fps = 60
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(pygame.Color('black'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEWHEEL:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode(monitor, pygame.FULLSCREEN)
                    sprite.image = pygame.transform.scale(img, (width * (monitor[1] / height), monitor[1]))
                    sprite.rect.x = (monitor[0] - width * (monitor[1] / height)) // 2
                else:
                    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
                    sprite.image = img
                    sprite.rect.x = 0

        all_sprites.draw(screen)

        pygame.display.flip()

    pygame.quit()
