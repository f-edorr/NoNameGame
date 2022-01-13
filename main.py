import pygame
from Img_Editor import ImgEditor

SIZE = WIDTH, HEIGHT = 700, 500

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('NoNameGame')
    monitor = [pygame.display.Info().current_w, pygame.display.Info().current_h]
    screen = pygame.display.set_mode(SIZE)
    editor = ImgEditor()
    pygame.display.set_icon(editor.load_image("icon.png", colorkey=-1))
    fullscreen = False

    # StartWindow
    background = pygame.sprite.Group()
    bckgnd = pygame.sprite.Sprite()
    bckgnd_img = editor.load_image("menu.png", f"\main_menu")
    bckgnd.image = bckgnd_img
    bckgnd.rect = bckgnd.image.get_rect()
    bckgnd.rect.x = 0
    bckgnd.rect.y = 0
    background.add(bckgnd)

    buttons = pygame.sprite.Group()
    start_btn = pygame.sprite.Sprite()
    start_btn_img = editor.load_image("start.png", f"\main_menu", -1)
    start_btn.image = start_btn_img
    upload_btn = pygame.sprite.Sprite()  # тут нужна функция какая-то
    upload_btn_img = editor.load_image("upload.png", f"\main_menu", -1)
    upload_btn.image = upload_btn_img
    exit_btn = pygame.sprite.Sprite()
    exit_btn_img = editor.load_image("exit.png", f"\main_menu", -1)
    exit_btn.image = exit_btn_img
    fs_btn = pygame.sprite.Sprite()
    fs_btn_img = editor.load_image("fs_btn1.png", f"\main_menu", -1)
    fs_btn.image = fs_btn_img
    fs_btn.rect = fs_btn.image.get_rect()
    fs_btn.rect.x = bckgnd.rect[2] - 50
    fs_btn.rect.y = 25
    buttons.add(fs_btn)

    running = True

    while running:
        screen.fill(pygame.Color('black'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and (fs_btn.rect.x + fs_btn.rect[2]) >= \
                    event.pos[0] >= fs_btn.rect.x and (fs_btn.rect.y + fs_btn.rect[3]) >= event.pos[
                1] >= fs_btn.rect.y and not fullscreen:
                fullscreen = True
                screen = pygame.display.set_mode(monitor, pygame.FULLSCREEN)

                bckgnd.image = editor.enhance_image(bckgnd_img, monitor[1] / HEIGHT)
                bckgnd.rect = bckgnd.image.get_rect()
                bckgnd.rect.x = (monitor[0] - WIDTH * (monitor[1] / HEIGHT)) // 2

                fs_btn.image = editor.load_image("fs_btn2.png", f"\main_menu", -1)
                fs_btn.image = editor.enhance_image(fs_btn.image, monitor[1] / HEIGHT)  # тут тоже функция нужна
                fs_btn.rect = fs_btn.image.get_rect()
                fs_btn.rect.x = bckgnd.rect[2] + (monitor[0] - WIDTH * (monitor[1] / HEIGHT)) // 2 - 25 - 43
                fs_btn.rect.y = 25

            if ((event.type == pygame.KEYDOWN and event.scancode == 41 ) or event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and (fs_btn.rect.x + fs_btn.rect[2]) >= \
                    event.pos[0] >= fs_btn.rect.x and (fs_btn.rect.y + fs_btn.rect[3]) >= event.pos[
                1] >= fs_btn.rect.y) and fullscreen:
                fullscreen = False
                screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
                bckgnd.image = bckgnd_img
                bckgnd.rect = bckgnd.image.get_rect()
                bckgnd.rect.x = 0

                fs_btn.image = editor.load_image("fs_btn1.png", f"\main_menu", -1)
                fs_btn.image = fs_btn_img
                fs_btn.rect = fs_btn.image.get_rect()
                fs_btn.rect.x = bckgnd.rect[2] - 50
                fs_btn.rect.y = 25

        background.draw(screen)
        buttons.draw(screen)

        pygame.display.flip()

    running = True

    pygame.quit()
