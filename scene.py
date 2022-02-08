import pygame

from player import Player
from Img_Editor import ImgEditor
from button import Button
from world_sprite import WorldSprite

SIZE = WIDTH, HEIGHT = 700, 500


class Scene:
    def __init__(self, monitor, parent_fs):
        self.monitor = monitor
        self.screen = pygame.display.get_surface()
        self.running = True
        self.fullscreen = False
        self.parent_fs = parent_fs

        self.jack_dialog = False

        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        self.bckgnd = pygame.sprite.Sprite()
        self.bckgnd_img = ImgEditor.enhance_image(ImgEditor.load_image("background.png", f"\scene1"), 2)
        self.new_sprite(self.bckgnd, self.bckgnd_img, 0, 0)
        self.border = pygame.sprite.Sprite()
        self.border_img = ImgEditor.enhance_image(ImgEditor.load_image("border.png", f"\scene1", (255, 255, 255)), 2)
        self.new_sprite(self.border, self.border_img, 0, 0)
        self.border.mask = pygame.mask.from_surface(self.border_img)

        self.visible_sprites.add(self.bckgnd, self.border)

        self.buttons = pygame.sprite.Group()
        self.fs_btn_img = ImgEditor.load_image("fs_btn1.png", f"\main_menu", -1)
        self.fs_btn = Button(self.fs_btn_img, self.bckgnd.rect[2] - 50, 25)

        self.buttons.add(self.fs_btn)

        self.tree_img = ImgEditor.enhance_image(ImgEditor.load_image("tree.png", f"\world_sprites", -1), 2)
        self.tree = WorldSprite(self.tree_img, 400, 100)

        self.lake_img = ImgEditor.enhance_image(ImgEditor.load_image("lake.png", f"\world_sprites", -1), 2)
        self.lake = WorldSprite(self.lake_img, 200, 130)

        self.bush_img = ImgEditor.enhance_image(ImgEditor.load_image("bush.png", f"\world_sprites", -1), 2)
        self.bush1 = WorldSprite(self.bush_img, 127, 245)
        self.bush2 = WorldSprite(self.bush_img, 370, 372)

        self.jack_img = ImgEditor.enhance_image(ImgEditor.load_image("jack.png", f"\world_sprites", -1), 2)
        self.jack = WorldSprite(self.jack_img, 435, 245, "Hi!",
                                ImgEditor.enhance_image(ImgEditor.load_image("jack.png", f"\characters", -1), 3))

        self.visible_sprites.add(self.tree, self.lake, self.bush1, self.bush2, self.jack)

        self.main_ch_sheet = ImgEditor.enhance_image(ImgEditor.load_image("main_animation.png", "", -1), 2)
        self.player = Player(self.main_ch_sheet, 300, 300)

        self.visible_sprites.add(self.player)

    def run(self):
        while self.running:
            self.screen.fill(pygame.Color('black'))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return -1, self.fullscreen

                if (self.fs_btn.is_clicked(event) and not self.fullscreen) or self.parent_fs:
                    self.parent_fs = False
                    self.fullscreen = True
                    self.screen = pygame.display.set_mode(self.monitor, pygame.FULLSCREEN)

                    new_image = ImgEditor.enhance_image(self.bckgnd_img, self.monitor[1] / HEIGHT)
                    self.fs_btn_clicked(self.bckgnd, new_image,
                                        (self.monitor[0] - WIDTH * (self.monitor[1] / HEIGHT)) // 2, 0)

                    new_image = ImgEditor.enhance_image(self.border_img, self.monitor[1] / HEIGHT)
                    self.fs_btn_clicked(self.border, new_image,
                                        (self.monitor[0] - WIDTH * (self.monitor[1] / HEIGHT)) // 2, 0)

                    new_image = ImgEditor.enhance_image(ImgEditor.load_image("fs_btn2.png", f"\main_menu", -1),
                                                        self.monitor[1] / HEIGHT)
                    self.fs_btn_clicked(self.fs_btn, new_image,
                                        self.monitor[0] - 25 - new_image.get_width() - (
                                                (self.monitor[0] - WIDTH * (self.monitor[1] / HEIGHT)) // 2), 25)

                    new_image = ImgEditor.enhance_image(self.tree_img, self.monitor[1] / HEIGHT)
                    self.fs_btn_clicked(self.tree, new_image, 850, 180)

                    new_image = ImgEditor.enhance_image(self.lake_img, self.monitor[1] / HEIGHT)
                    self.fs_btn_clicked(self.lake, new_image, 510, 225)

                    new_image = ImgEditor.enhance_image(self.jack_img, self.monitor[1] / HEIGHT)
                    self.fs_btn_clicked(self.jack, new_image, 880, 425)

                    new_image = ImgEditor.enhance_image(self.bush_img, self.monitor[1] / HEIGHT)
                    self.fs_btn_clicked(self.bush1, new_image, 381, 426)
                    self.fs_btn_clicked(self.bush2, new_image, 800, 645)

                    new_image = ImgEditor.enhance_image(self.main_ch_sheet, self.monitor[1] / HEIGHT)
                    self.main_ch.fs_update(new_image, self.main_ch.x * self.monitor[1] / HEIGHT,
                                           self.main_ch.y * self.monitor[1] / HEIGHT)


                elif ((event.type == pygame.KEYDOWN and event.scancode == 41) or
                      self.fs_btn.is_clicked(event)) and self.fullscreen:
                    self.fullscreen = False
                    self.screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)

                    self.fs_btn_clicked(self.bckgnd, self.bckgnd_img, 0, 0)
                    self.fs_btn_clicked(self.border, self.border_img, 0, 0)

                    fs_btn_img = ImgEditor.load_image("fs_btn1.png", f"\main_menu", -1)
                    self.fs_btn_clicked(self.fs_btn, fs_btn_img, self.bckgnd.rect[2] - 50, 25)

                    self.fs_btn_clicked(self.tree, self.tree_img, 400, 100)
                    self.fs_btn_clicked(self.lake, self.lake_img, 200, 130)
                    self.fs_btn_clicked(self.bush1, self.bush_img, 127, 245)
                    self.fs_btn_clicked(self.bush2, self.bush_img, 370, 372)
                    self.fs_btn_clicked(self.jack, self.jack_img, 435, 245)

                    self.player.fs_update(self.main_ch_sheet, self.player.x // (self.monitor[1] / HEIGHT),
                                           self.player.y // (self.monitor[1] / HEIGHT))

                if event.type == pygame.KEYDOWN and event.scancode == 8 and pygame.sprite.collide_mask(self.player,
                                                                                                       self.jack):
                    self.jack_dialog = True
                if self.jack.dialog.is_clicked(event):
                    self.jack_dialog = False

            self.draw_scene()
            pygame.display.flip()

    def fs_btn_clicked(self, sprite, image, x, y):
        sprite.image = image
        sprite.rect = sprite.image.get_rect()
        sprite.rect.x = x
        sprite.rect.y = y

    def new_sprite(self, sprite, image, x, y):
        sprite.image = image
        sprite.rect = image.get_rect()
        sprite.rect.x = x
        sprite.rect.y = y

    def draw_scene(self):

        self.visible_sprites.draw(self.screen)
        self.buttons.draw(self.screen)

        self.visible_sprites.update()
        if self.jack_dialog:
            self.jack.draw_dialog(self.fullscreen, self.screen, self.monitor)
