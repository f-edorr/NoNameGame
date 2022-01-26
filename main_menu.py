import pygame
from Img_Editor import ImgEditor
from button import Button

SIZE = WIDTH, HEIGHT = 700, 500


class MainMenu:
    def __init__(self, screen, monitor):
        self.monitor = monitor
        self.screen = screen
        self.running = True
        self.fullscreen = False
        self.new_game = False
        self.enter = False
        self.text = ""
        # StartWindow

        self.background = pygame.sprite.Group()
        self.bckgnd = pygame.sprite.Sprite()
        self.bckgnd_img = ImgEditor.load_image("menu.png", f"\main_menu")
        self.new_sprite(self.bckgnd, self.bckgnd_img, 0, 0)
        self.background.add(self.bckgnd)

        self.buttons = pygame.sprite.Group()

        self.start_btn_img = ImgEditor.enhance_image(ImgEditor.load_image("start.png", f"\main_menu", -1), 3)
        self.start_btn = Button(self.start_btn_img, WIDTH // 2 - self.start_btn_img.get_width() // 2,
                                HEIGHT // 2 - self.start_btn_img.get_height() // 2)

        self.upload_btn_img = ImgEditor.enhance_image(ImgEditor.load_image("upload.png", f"\main_menu", -1), 3)
        self.upload_btn = Button(self.upload_btn_img, WIDTH // 2 - self.upload_btn_img.get_width() // 2,
                                 HEIGHT // 2 - self.upload_btn_img.get_height() // 2 + self.upload_btn_img.get_height() + 10)

        self.exit_btn_img = ImgEditor.enhance_image(ImgEditor.load_image("exit.png", f"\main_menu", -1), 3)
        self.exit_btn = Button(self.exit_btn_img, WIDTH // 2 - self.exit_btn_img.get_width() // 2,
                               HEIGHT // 2 - self.exit_btn_img.get_height() // 2 + self.upload_btn_img.get_height() + 10 + self.exit_btn_img.get_height() + 10)

        self.fs_btn_img = ImgEditor.load_image("fs_btn1.png", f"\main_menu", -1)
        self.fs_btn = Button(self.fs_btn_img, self.bckgnd.rect[2] - 50, 25)

        self.buttons.add(self.fs_btn, self.start_btn, self.upload_btn, self.exit_btn)

        # New game window
        self.new_game_group = pygame.sprite.Group()

        self.new_game_bck_img = ImgEditor.enhance_image(ImgEditor.load_image("new_game.png", f"\main_menu", -1), 1.5)
        self.new_game_bck = Button(self.new_game_bck_img, WIDTH // 2 - self.new_game_bck_img.get_width() // 2,
                                   HEIGHT // 2 - self.new_game_bck_img.get_height() // 2)

        self.back_btn_img = ImgEditor.enhance_image(ImgEditor.load_image("back_btn.png", f"\main_menu", -1), 1)
        self.back_btn = Button(self.back_btn_img,
                               self.new_game_bck.rect.x + self.new_game_bck_img.get_width() - self.back_btn_img.get_width() - 25,
                               self.new_game_bck.rect.y + 25)

        self.enter_btn_img = ImgEditor.enhance_image(ImgEditor.load_image("enter1.png", f"\main_menu", -1), 3)
        self.enter_btn = Button(self.enter_btn_img,
                                self.new_game_bck.rect.x + self.new_game_bck_img.get_width() // 2 - self.enter_btn_img.get_width() // 2,
                                self.new_game_bck.rect.y + self.new_game_bck_img.get_height() // 2)

        self.begin_btn_img = ImgEditor.enhance_image(ImgEditor.load_image("begin.png", f"\main_menu", -1), 3)
        self.begin_btn = Button(self.begin_btn_img,
                                self.new_game_bck.rect.x + self.new_game_bck_img.get_width() // 2 - self.begin_btn_img.get_width() // 2,
                                self.new_game_bck.rect.y + self.new_game_bck_img.get_height() // 4 * 3)

        self.new_game_group.add(self.new_game_bck, self.back_btn, self.enter_btn, self.begin_btn)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if self.new_game:
                    if self.back_btn.is_mouse_on() or self.enter_btn.is_mouse_on() or self.begin_btn.is_mouse_on():
                        pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
                    else:
                        pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))
                    if event.type == pygame.QUIT:
                        self.running = False
                        return -1, self.fullscreen

                    if self.back_btn.is_clicked(event):
                        self.new_game = False

                    if self.enter_btn.is_clicked(event):
                        self.enter_btn.image = ImgEditor.enhance_image(
                            ImgEditor.load_image("enter2.png", f"\main_menu", -1), 3)
                        self.enter = True
                        if self.fullscreen:
                            self.enter_btn.image = ImgEditor.enhance_image(self.enter_btn.image,
                                                                           self.monitor[1] / HEIGHT)

                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        self.enter_btn.image = ImgEditor.enhance_image(
                            ImgEditor.load_image("enter1.png", f"\main_menu", -1), 3)
                        self.enter = False

                        if self.fullscreen:
                            self.enter_btn.image = ImgEditor.enhance_image(self.enter_btn.image,
                                                                           self.monitor[1] / HEIGHT)

                    if event.type == pygame.KEYDOWN and self.enter:
                        if event.scancode == 42:
                            if len(self.text) > 0:
                                self.text = self.text[:-1]

                        if len(self.text) < 9 and 29 >= event.scancode >= 4:
                            self.text += event.unicode

                    if self.begin_btn.is_clicked(event):
                        return 1, self.fullscreen

                else:
                    if self.fs_btn.is_mouse_on() or self.start_btn.is_mouse_on() or self.upload_btn.is_mouse_on() or self.exit_btn.is_mouse_on():
                        pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
                    else:
                        pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))
                    if event.type == pygame.QUIT or self.exit_btn.is_clicked(event):
                        self.running = False
                        return -1, self.fullscreen

                    if self.start_btn.is_clicked(event):
                        self.new_game = True
                        self.text = ""

                    if self.fs_btn.is_clicked(event) and not self.fullscreen:
                        self.fullscreen = True
                        self.screen = pygame.display.set_mode(self.monitor, pygame.FULLSCREEN)

                        new_image = ImgEditor.enhance_image(self.bckgnd_img, self.monitor[1] / HEIGHT)
                        self.fs_btn_clicked(self.bckgnd, new_image,
                                            (self.monitor[0] - WIDTH * (self.monitor[1] / HEIGHT)) // 2, 0)

                        new_image = ImgEditor.enhance_image(ImgEditor.load_image("fs_btn2.png", f"\main_menu", -1),
                                                            self.monitor[1] / HEIGHT)

                        self.fs_btn_clicked(self.fs_btn, new_image,
                                            self.monitor[0] - 25 - new_image.get_width() - (
                                                    (self.monitor[0] - WIDTH * (self.monitor[1] / HEIGHT)) // 2), 25)

                        new_image = ImgEditor.enhance_image(self.start_btn_img, self.monitor[1] / HEIGHT)
                        self.fs_btn_clicked(self.start_btn, new_image,
                                            self.monitor[0] / 2 - new_image.get_width() / 2,
                                            self.monitor[1] / 2 - new_image.get_height() / 2)

                        new_image = ImgEditor.enhance_image(self.upload_btn_img, self.monitor[1] / HEIGHT)
                        self.fs_btn_clicked(self.upload_btn, new_image,
                                            self.monitor[0] / 2 - new_image.get_width() / 2,
                                            self.monitor[
                                                1] / 2 - new_image.get_height() / 2 + 10 + new_image.get_height())

                        new_image = ImgEditor.enhance_image(self.exit_btn_img, self.monitor[1] / HEIGHT)
                        self.fs_btn_clicked(self.exit_btn, new_image,
                                            self.monitor[0] / 2 - new_image.get_width() / 2,
                                            self.monitor[
                                                1] / 2 - new_image.get_height() / 2 + 20 + new_image.get_height()
                                            + self.upload_btn.image.get_height())

                        new_image = ImgEditor.enhance_image(self.new_game_bck_img, self.monitor[1] / HEIGHT)
                        self.fs_btn_clicked(self.new_game_bck, new_image,
                                            self.monitor[0] // 2 - new_image.get_width() // 2,
                                            self.monitor[1] // 2 - new_image.get_height() // 2)

                        new_image = ImgEditor.enhance_image(self.back_btn_img, self.monitor[1] / HEIGHT)
                        self.fs_btn_clicked(self.back_btn, new_image,
                                            self.new_game_bck.rect.x + self.new_game_bck.rect[
                                                2] - new_image.get_width() - 25,
                                            self.new_game_bck.rect.y + 25)

                        new_image = ImgEditor.enhance_image(self.enter_btn_img, self.monitor[1] / HEIGHT)
                        self.fs_btn_clicked(self.enter_btn, new_image,
                                            self.new_game_bck.rect.x + self.new_game_bck.rect[
                                                2] // 2 - new_image.get_width() // 2,
                                            self.new_game_bck.rect.y + self.new_game_bck.rect[3] // 2)

                        new_image = ImgEditor.enhance_image(self.begin_btn_img, self.monitor[1] / HEIGHT)
                        self.fs_btn_clicked(self.begin_btn, new_image,
                                            self.new_game_bck.rect.x + self.new_game_bck.rect[
                                                2] // 2 - new_image.get_width() // 2,
                                            self.new_game_bck.rect.y + self.new_game_bck.rect[3] // 4 * 3)

                    if ((event.type == pygame.KEYDOWN and event.scancode == 41) or
                        self.fs_btn.is_clicked(event)) and self.fullscreen:
                        self.fullscreen = False
                        self.screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)

                        self.fs_btn_clicked(self.bckgnd, self.bckgnd_img, 0, 0)

                        fs_btn_img = ImgEditor.load_image("fs_btn1.png", f"\main_menu", -1)
                        self.fs_btn_clicked(self.fs_btn, fs_btn_img, self.bckgnd.rect[2] - 50, 25)

                        self.fs_btn_clicked(self.start_btn, self.start_btn_img,
                                            WIDTH // 2 - self.start_btn_img.get_width() // 2,
                                            HEIGHT // 2 - self.start_btn_img.get_height() // 2)

                        self.fs_btn_clicked(self.upload_btn, self.upload_btn_img,
                                            WIDTH // 2 - self.upload_btn_img.get_width() // 2,
                                            HEIGHT // 2 - self.upload_btn_img.get_height() // 2 + 10 + self.upload_btn_img.get_height())

                        self.fs_btn_clicked(self.exit_btn, self.exit_btn_img,
                                            WIDTH // 2 - self.exit_btn_img.get_width() // 2,
                                            HEIGHT // 2 - self.exit_btn_img.get_height() // 2 + 20 + self.upload_btn_img.get_height()
                                            + self.exit_btn_img.get_height())

                        self.fs_btn_clicked(self.new_game_bck, self.new_game_bck_img,
                                            WIDTH // 2 - self.new_game_bck_img.get_width() // 2,
                                            HEIGHT // 2 - self.new_game_bck_img.get_height() // 2)

                        self.fs_btn_clicked(self.back_btn, self.back_btn_img,
                                            self.new_game_bck.rect.x + self.new_game_bck_img.get_width() - self.back_btn_img.get_width() - 25,
                                            self.new_game_bck.rect.y + 25)

                        self.fs_btn_clicked(self.enter_btn, self.enter_btn_img,
                                            self.new_game_bck.rect.x + self.new_game_bck_img.get_width() // 2 - self.enter_btn_img.get_width() // 2,
                                            self.new_game_bck.rect.y + self.new_game_bck_img.get_height() // 2)

                        self.fs_btn_clicked(self.begin_btn, self.begin_btn_img,
                                            self.new_game_bck.rect.x + self.new_game_bck_img.get_width() // 2 - self.begin_btn_img.get_width() // 2,
                                            self.new_game_bck.rect.y + self.new_game_bck_img.get_height() // 4 * 3)

            self.draw_scene()
            pygame.display.flip()

    def draw_scene(self):
        self.background.draw(self.screen)
        self.buttons.draw(self.screen)
        if self.new_game:
            self.new_game_group.draw(self.screen)
            if self.text != "":
                if not self.fullscreen:
                    font = pygame.font.SysFont('Comic Sans MS', 20)
                    self.screen.blit(font.render(self.text, False, (47, 29, 113)),
                                     (self.enter_btn.rect.x + 5, self.enter_btn.rect.y + 5))
                if self.fullscreen:
                    font = pygame.font.SysFont('Comic Sans MS', 40)
                    self.screen.blit(font.render(self.text, False, (47, 29, 113)),
                                     (self.enter_btn.rect.x + 10, self.enter_btn.rect.y + 4))

    def new_sprite(self, sprite, image, x, y):
        sprite.image = image
        sprite.rect = image.get_rect()
        sprite.rect.x = x
        sprite.rect.y = y

    def fs_btn_clicked(self, sprite, image, x, y):
        sprite.image = image
        sprite.rect = sprite.image.get_rect()
        sprite.rect.x = x
        sprite.rect.y = y
