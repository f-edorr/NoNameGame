import pygame
from Img_Editor import ImgEditor

SIZE = WIDTH, HEIGHT = 700, 500


def new_sprite(sprite, image, x, y):
    sprite.image = image
    sprite.rect = image.get_rect()
    sprite.rect.x = x
    sprite.rect.y = y


def fs_btn_clicked(sprite, image, x, y):
    sprite.image = image
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = x
    sprite.rect.y = y


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('NoNameGame')
    monitor = [pygame.display.Info().current_w, pygame.display.Info().current_h]
    screen = pygame.display.set_mode(SIZE)
    editor = ImgEditor()
    pygame.display.set_icon(editor.load_image("icon.png", colorkey=-1))
    fullscreen = False
    new_game = False

    # StartWindow
    background = pygame.sprite.Group()
    bckgnd = pygame.sprite.Sprite()
    bckgnd_img = editor.load_image("menu.png", f"\main_menu")
    new_sprite(bckgnd, bckgnd_img, 0, 0)
    background.add(bckgnd)

    buttons = pygame.sprite.Group()
    start_btn = pygame.sprite.Sprite()
    start_btn_img = editor.enhance_image(editor.load_image("start.png", f"\main_menu", -1), 3)
    start_btn.image = start_btn_img
    new_sprite(start_btn, start_btn_img, WIDTH // 2 - start_btn_img.get_width() // 2,
               HEIGHT // 2 - start_btn_img.get_height() // 2)

    upload_btn = pygame.sprite.Sprite()
    upload_btn_img = editor.enhance_image(editor.load_image("upload.png", f"\main_menu", -1), 3)
    new_sprite(upload_btn, upload_btn_img, WIDTH // 2 - upload_btn_img.get_width() // 2,
               HEIGHT // 2 - upload_btn_img.get_height() // 2 + upload_btn_img.get_height() + 10)

    exit_btn = pygame.sprite.Sprite()
    exit_btn_img = editor.enhance_image(editor.load_image("exit.png", f"\main_menu", -1), 3)
    new_sprite(exit_btn, exit_btn_img, WIDTH // 2 - exit_btn_img.get_width() // 2,
               HEIGHT // 2 - exit_btn_img.get_height() // 2 + upload_btn_img.get_height() + 10 + exit_btn_img.get_height() + 10)

    fs_btn = pygame.sprite.Sprite()
    fs_btn_img = editor.load_image("fs_btn1.png", f"\main_menu", -1)
    new_sprite(fs_btn, fs_btn_img, bckgnd.rect[2] - 50, 25)
    buttons.add(fs_btn, start_btn, upload_btn, exit_btn)

    # New game window



    running = True

    while running:
        screen.fill(pygame.Color('black'))
        for event in pygame.event.get():

            if event.type == pygame.QUIT or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and (
                    exit_btn.rect.x + exit_btn.rect[2]) >=
                                             event.pos[0] >= exit_btn.rect.x and (exit_btn.rect.y + exit_btn.rect[3]) >=
                                             event.pos[
                                                 1] >= exit_btn.rect.y):
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and (
                    start_btn.rect.x + start_btn.rect[2]) >= event.pos[0] >= start_btn.rect.x and (
                    start_btn.rect.y + start_btn.rect[3]) >= event.pos[
                1] >= start_btn.rect.y:
                new_game = True

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and (fs_btn.rect.x + fs_btn.rect[2]) >= \
                    event.pos[0] >= fs_btn.rect.x and (fs_btn.rect.y + fs_btn.rect[3]) >= event.pos[
                1] >= fs_btn.rect.y and not fullscreen:
                fullscreen = True
                screen = pygame.display.set_mode(monitor, pygame.FULLSCREEN)

                new_image = editor.enhance_image(bckgnd_img, monitor[1] / HEIGHT)
                fs_btn_clicked(bckgnd, new_image,
                               (monitor[0] - WIDTH * (monitor[1] / HEIGHT)) // 2, 0)

                new_image = editor.enhance_image(editor.load_image("fs_btn2.png", f"\main_menu", -1),
                                                 monitor[1] / HEIGHT)

                fs_btn_clicked(fs_btn, new_image,
                               monitor[0] - 25 - new_image.get_width() - (
                                       (monitor[0] - WIDTH * (monitor[1] / HEIGHT)) // 2), 25)

                new_image = editor.enhance_image(start_btn_img, monitor[1] / HEIGHT)
                fs_btn_clicked(start_btn, new_image,
                               monitor[0] / 2 - new_image.get_width() / 2,
                               monitor[1] / 2 - new_image.get_height() / 2)

                new_image = editor.enhance_image(upload_btn_img, monitor[1] / HEIGHT)
                fs_btn_clicked(upload_btn, new_image,
                               monitor[0] / 2 - new_image.get_width() / 2,
                               monitor[1] / 2 - new_image.get_height() / 2 + 10 + new_image.get_height())

                new_image = editor.enhance_image(exit_btn_img, monitor[1] / HEIGHT)
                fs_btn_clicked(exit_btn, new_image,
                               monitor[0] / 2 - new_image.get_width() / 2,
                               monitor[1] / 2 - new_image.get_height() / 2 + 20 + new_image.get_height()
                               + upload_btn.image.get_height())

            if ((event.type == pygame.KEYDOWN and event.scancode == 41) or
                event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and (
                        fs_btn.rect.x + fs_btn.rect[2]) >=
                event.pos[0] >= fs_btn.rect.x and (fs_btn.rect.y + fs_btn.rect[3]) >= event.pos[
                    1] >= fs_btn.rect.y) and fullscreen:
                fullscreen = False
                screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)

                fs_btn_clicked(bckgnd, bckgnd_img, 0, 0)

                fs_btn_img = editor.load_image("fs_btn1.png", f"\main_menu", -1)
                fs_btn_clicked(fs_btn, fs_btn_img, bckgnd.rect[2] - 50, 25)

                fs_btn_clicked(start_btn, start_btn_img, WIDTH // 2 - start_btn_img.get_width() // 2,
                               HEIGHT // 2 - start_btn_img.get_height() // 2)

                fs_btn_clicked(upload_btn, upload_btn_img, WIDTH // 2 - upload_btn_img.get_width() // 2,
                               HEIGHT // 2 - upload_btn_img.get_height() // 2 + 10 + upload_btn_img.get_height())

                fs_btn_clicked(exit_btn, exit_btn_img, WIDTH // 2 - exit_btn_img.get_width() // 2,
                               HEIGHT // 2 - exit_btn_img.get_height() // 2 + 20 + upload_btn_img.get_height()
                               + exit_btn_img.get_height())

        background.draw(screen)
        buttons.draw(screen)

        pygame.display.flip()

    running = True

    pygame.quit()
