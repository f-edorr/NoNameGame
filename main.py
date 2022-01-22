import pygame
from Img_Editor import ImgEditor
from button import Button

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
    pygame.display.set_icon(ImgEditor.load_image("icon.png", colorkey=-1))
    fullscreen = False
    new_game = False

    # StartWindow
    background = pygame.sprite.Group()
    bckgnd = pygame.sprite.Sprite()
    bckgnd_img = ImgEditor.load_image("menu.png", f"\main_menu")
    new_sprite(bckgnd, bckgnd_img, 0, 0)
    background.add(bckgnd)

    buttons = pygame.sprite.Group()

    start_btn_img = ImgEditor.enhance_image(ImgEditor.load_image("start.png", f"\main_menu", -1), 3)
    start_btn = Button(start_btn_img, WIDTH // 2 - start_btn_img.get_width() // 2,
                       HEIGHT // 2 - start_btn_img.get_height() // 2)

    upload_btn_img = ImgEditor.enhance_image(ImgEditor.load_image("upload.png", f"\main_menu", -1), 3)
    upload_btn = Button(upload_btn_img, WIDTH // 2 - upload_btn_img.get_width() // 2,
                        HEIGHT // 2 - upload_btn_img.get_height() // 2 + upload_btn_img.get_height() + 10)

    exit_btn_img = ImgEditor.enhance_image(ImgEditor.load_image("exit.png", f"\main_menu", -1), 3)
    exit_btn = Button(exit_btn_img, WIDTH // 2 - exit_btn_img.get_width() // 2,
                      HEIGHT // 2 - exit_btn_img.get_height() // 2 + upload_btn_img.get_height() + 10 + exit_btn_img.get_height() + 10)

    fs_btn_img = ImgEditor.load_image("fs_btn1.png", f"\main_menu", -1)
    fs_btn = Button(fs_btn_img, bckgnd.rect[2] - 50, 25)

    buttons.add(fs_btn, start_btn, upload_btn, exit_btn)

    # New game window
    new_game_group = pygame.sprite.Group()

    new_game_bck_img = ImgEditor.enhance_image(ImgEditor.load_image("new_game.png", f"\main_menu", -1), 1.5)
    new_game_bck = Button(new_game_bck_img, WIDTH // 2 - new_game_bck_img.get_width() // 2,
                          HEIGHT // 2 - new_game_bck_img.get_height() // 2)

    back_btn_img = ImgEditor.enhance_image(ImgEditor.load_image("back_btn.png", f"\main_menu", -1), 1)
    back_btn = Button(back_btn_img, new_game_bck.rect.x + new_game_bck_img.get_width() - back_btn_img.get_width() - 25,
                      new_game_bck.rect.y + 25)

    enter_btn_img = ImgEditor.enhance_image(ImgEditor.load_image("enter1.png", f"\main_menu", -1), 3)
    enter_btn = Button(enter_btn_img,
                       new_game_bck.rect.x + new_game_bck_img.get_width() // 2 - enter_btn_img.get_width() // 2,
                       new_game_bck.rect.y + new_game_bck_img.get_height() // 2)

    begin_btn_img = ImgEditor.enhance_image(ImgEditor.load_image("begin.png", f"\main_menu", -1), 3)
    begin_btn = Button(begin_btn_img,
                       new_game_bck.rect.x + new_game_bck_img.get_width() // 2 - begin_btn_img.get_width() // 2,
                       new_game_bck.rect.y + new_game_bck_img.get_height() // 4 * 3)

    new_game_group.add(new_game_bck, back_btn, enter_btn, begin_btn)

    running = True

    while running:
        screen.fill(pygame.Color('black'))
        for event in pygame.event.get():

            if new_game:
                if event.type == pygame.QUIT:
                    running = False
                if back_btn.is_clicked(event):
                    new_game = False
                if enter_btn.is_clicked(event):
                    enter_btn.image = ImgEditor.enhance_image(ImgEditor.load_image("enter2.png", f"\main_menu", -1), 3)
                    if fullscreen:
                        enter_btn.image = ImgEditor.enhance_image(enter_btn.image, monitor[1] / HEIGHT)
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    enter_btn.image = ImgEditor.enhance_image(ImgEditor.load_image("enter1.png", f"\main_menu", -1), 3)
                    if fullscreen:
                        enter_btn.image = ImgEditor.enhance_image(enter_btn.image, monitor[1] / HEIGHT)




            else:
                if event.type == pygame.QUIT or exit_btn.is_clicked(event):
                    running = False

                if start_btn.is_clicked(event):
                    new_game = True

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and (fs_btn.rect.x + fs_btn.rect[2]) >= \
                        event.pos[0] >= fs_btn.rect.x and (fs_btn.rect.y + fs_btn.rect[3]) >= event.pos[
                    1] >= fs_btn.rect.y and not fullscreen:
                    fullscreen = True
                    screen = pygame.display.set_mode(monitor, pygame.FULLSCREEN)

                    new_image = ImgEditor.enhance_image(bckgnd_img, monitor[1] / HEIGHT)
                    fs_btn_clicked(bckgnd, new_image,
                                   (monitor[0] - WIDTH * (monitor[1] / HEIGHT)) // 2, 0)

                    new_image = ImgEditor.enhance_image(ImgEditor.load_image("fs_btn2.png", f"\main_menu", -1),
                                                     monitor[1] / HEIGHT)

                    fs_btn_clicked(fs_btn, new_image,
                                   monitor[0] - 25 - new_image.get_width() - (
                                           (monitor[0] - WIDTH * (monitor[1] / HEIGHT)) // 2), 25)

                    new_image = ImgEditor.enhance_image(start_btn_img, monitor[1] / HEIGHT)
                    fs_btn_clicked(start_btn, new_image,
                                   monitor[0] / 2 - new_image.get_width() / 2,
                                   monitor[1] / 2 - new_image.get_height() / 2)

                    new_image = ImgEditor.enhance_image(upload_btn_img, monitor[1] / HEIGHT)
                    fs_btn_clicked(upload_btn, new_image,
                                   monitor[0] / 2 - new_image.get_width() / 2,
                                   monitor[1] / 2 - new_image.get_height() / 2 + 10 + new_image.get_height())

                    new_image = ImgEditor.enhance_image(exit_btn_img, monitor[1] / HEIGHT)
                    fs_btn_clicked(exit_btn, new_image,
                                   monitor[0] / 2 - new_image.get_width() / 2,
                                   monitor[1] / 2 - new_image.get_height() / 2 + 20 + new_image.get_height()
                                   + upload_btn.image.get_height())

                    new_image = ImgEditor.enhance_image(new_game_bck_img, monitor[1] / HEIGHT)
                    fs_btn_clicked(new_game_bck, new_image, monitor[0] // 2 - new_image.get_width() // 2,
                                   monitor[1] // 2 - new_image.get_height() // 2)

                    new_image = ImgEditor.enhance_image(back_btn_img, monitor[1] / HEIGHT)
                    fs_btn_clicked(back_btn, new_image,
                                   new_game_bck.rect.x + new_game_bck.rect[2] - new_image.get_width() - 25,
                                   new_game_bck.rect.y + 25)

                    new_image = ImgEditor.enhance_image(enter_btn_img, monitor[1] / HEIGHT)
                    fs_btn_clicked(enter_btn, new_image,
                                   new_game_bck.rect.x + new_game_bck.rect[2] // 2 - new_image.get_width() // 2,
                                   new_game_bck.rect.y + new_game_bck.rect[3] // 2)

                    new_image = ImgEditor.enhance_image(begin_btn_img, monitor[1] / HEIGHT)
                    fs_btn_clicked(begin_btn, new_image,
                                   new_game_bck.rect.x + new_game_bck.rect[2] // 2 - new_image.get_width() // 2,
                                   new_game_bck.rect.y + new_game_bck.rect[3] // 4 * 3)

                if ((event.type == pygame.KEYDOWN and event.scancode == 41) or
                    event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and (
                            fs_btn.rect.x + fs_btn.rect[2]) >=
                    event.pos[0] >= fs_btn.rect.x and (fs_btn.rect.y + fs_btn.rect[3]) >= event.pos[
                        1] >= fs_btn.rect.y) and fullscreen:
                    fullscreen = False
                    screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)

                    fs_btn_clicked(bckgnd, bckgnd_img, 0, 0)

                    fs_btn_img = ImgEditor.load_image("fs_btn1.png", f"\main_menu", -1)
                    fs_btn_clicked(fs_btn, fs_btn_img, bckgnd.rect[2] - 50, 25)

                    fs_btn_clicked(start_btn, start_btn_img, WIDTH // 2 - start_btn_img.get_width() // 2,
                                   HEIGHT // 2 - start_btn_img.get_height() // 2)

                    fs_btn_clicked(upload_btn, upload_btn_img, WIDTH // 2 - upload_btn_img.get_width() // 2,
                                   HEIGHT // 2 - upload_btn_img.get_height() // 2 + 10 + upload_btn_img.get_height())

                    fs_btn_clicked(exit_btn, exit_btn_img, WIDTH // 2 - exit_btn_img.get_width() // 2,
                                   HEIGHT // 2 - exit_btn_img.get_height() // 2 + 20 + upload_btn_img.get_height()
                                   + exit_btn_img.get_height())

                    fs_btn_clicked(new_game_bck, new_game_bck_img, WIDTH // 2 - new_game_bck_img.get_width() // 2,
                                   HEIGHT // 2 - new_game_bck_img.get_height() // 2)

                    fs_btn_clicked(back_btn, back_btn_img,
                                   new_game_bck.rect.x + new_game_bck_img.get_width() - back_btn_img.get_width() - 25,
                                   new_game_bck.rect.y + 25)

                    fs_btn_clicked(enter_btn, enter_btn_img,
                                   new_game_bck.rect.x + new_game_bck_img.get_width() // 2 - enter_btn_img.get_width() // 2,
                                   new_game_bck.rect.y + new_game_bck_img.get_height() // 2)

                    fs_btn_clicked(begin_btn, begin_btn_img,
                                   new_game_bck.rect.x + new_game_bck_img.get_width() // 2 - begin_btn_img.get_width() // 2,
                                   new_game_bck.rect.y + new_game_bck_img.get_height() // 4 * 3)

        background.draw(screen)
        buttons.draw(screen)
        if new_game:
            new_game_group.draw(screen)

        pygame.display.flip()

    running = True

    pygame.quit()
