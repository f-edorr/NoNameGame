import pygame

from player import Player
from Img_Editor import ImgEditor
from button import Button
from world_sprite import WorldSprite

SIZE = WIDTH, HEIGHT = 700, 500
FPS = 60


class Scene_2:
    def __init__(self, monitor, parent_fs):
        file = open(f"./data/txts/player.txt", encoding="utf-8")
        data = file.read().split('\n')
        self.player_name = data[0]
        file.close()
        self.monitor = monitor
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.running = True
        self.fullscreen = False
        self.parent_fs = parent_fs

        self.john_dialog = False

        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        self.bckgnd = pygame.sprite.Sprite()
        self.bckgnd_img = ImgEditor.enhance_image(ImgEditor.load_image("background.png", f"\scene2"), 2)
        self.new_sprite(self.bckgnd, self.bckgnd_img, 0, 0)
        self.border = pygame.sprite.Sprite()
        self.border_img = ImgEditor.enhance_image(ImgEditor.load_image("border.png", f"\scene2", (255, 255, 255)), 2)
        self.new_sprite(self.border, self.border_img, 0, 0)
        self.border.mask = pygame.mask.from_surface(self.border_img)

        self.visible_sprites.add(self.bckgnd, self.border)

        self.buttons = pygame.sprite.Group()
        self.fs_btn_img = ImgEditor.load_image("fs_btn_night_1.png", f"\main_menu", -1)
        self.fs_btn = Button(self.fs_btn_img, self.bckgnd.rect[2] - 50, 25)

        self.buttons.add(self.fs_btn)

        self.tree_img = ImgEditor.enhance_image(ImgEditor.load_image("fallen_tree.png", f"\world_sprites", -1), 2)
        self.tree = WorldSprite(self.tree_img, 271, 168)

        self.mushroom_img = ImgEditor.enhance_image(ImgEditor.load_image("mushroom.png", f"\world_sprites", -1), 2)
        self.mushroom = WorldSprite(self.mushroom_img, 470, 140)

        self.bush_img = ImgEditor.enhance_image(ImgEditor.load_image("bush_n.png", f"\world_sprites", -1), 2)
        self.bush1 = WorldSprite(self.bush_img, 175, 92)
        self.bush2 = WorldSprite(self.bush_img, 442, 370)

        self.fern1_img = ImgEditor.enhance_image(ImgEditor.load_image("fern1.png", f"\world_sprites", -1), 2)
        self.fern2_img = ImgEditor.enhance_image(ImgEditor.load_image("fern2.png", f"\world_sprites", -1), 2)
        self.fern1 = WorldSprite(self.fern1_img, 85, 303)
        self.fern2 = WorldSprite(self.fern2_img, 165, 345)

        self.john_img = ImgEditor.enhance_image(ImgEditor.load_image("john.png", f"\world_sprites", -1), 2)
        self.john = WorldSprite(self.john_img, 435, 245,
                                f"Привет, {self.player_name}! Рад тебя видеть! Я отправился искать\nсвой меч, и совсем заблудился.\nПомоги мне выбраться отсюда!",
                                ImgEditor.enhance_image(ImgEditor.load_image("john.png", f"\characters", -1), 3),
                                time='night')

        self.visible_sprites.add(self.tree, self.mushroom, self.bush1, self.bush2, self.john, self.fern1, self.fern2)

        self.obstacle_sprites.add(self.bush1, self.bush2, self.tree, self.mushroom, self.john, self.border, self.fern1,
                                  self.fern2)
        self.player = Player(300, 300, self.obstacle_sprites)

        self.visible_sprites.add(self.player)

    def run(self):
        while self.running:
            self.screen.fill(pygame.Color('black'))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return -1, self.fullscreen
                if event.type == pygame.KEYDOWN:
                    print(event.scancode)
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

                    new_image = ImgEditor.enhance_image(ImgEditor.load_image("fs_btn_night_2.png", f"\main_menu", -1),
                                                        self.monitor[1] / HEIGHT)
                    self.fs_btn_clicked(self.fs_btn, new_image,
                                        self.monitor[0] - 25 - new_image.get_width() - (
                                                (self.monitor[0] - WIDTH * (self.monitor[1] / HEIGHT)) // 2), 25)

                    new_image = ImgEditor.enhance_image(self.tree_img, self.monitor[1] / HEIGHT)
                    self.fs_btn_clicked(self.tree, new_image, 631, 292)

                    new_image = ImgEditor.enhance_image(self.mushroom_img, self.monitor[1] / HEIGHT)
                    self.fs_btn_clicked(self.mushroom, new_image, 955, 245)

                    new_image = ImgEditor.enhance_image(self.john_img, self.monitor[1] / HEIGHT)
                    self.fs_btn_clicked(self.john, new_image, 880, 425)

                    new_image = ImgEditor.enhance_image(self.bush_img, self.monitor[1] / HEIGHT)
                    self.fs_btn_clicked(self.bush1, new_image, 440, 157)
                    self.fs_btn_clicked(self.bush2, new_image, 925, 640)

                    new_image = ImgEditor.enhance_image(self.fern1_img, self.monitor[1] / HEIGHT)
                    self.fs_btn_clicked(self.fern1, new_image, 300, 527)

                    new_image = ImgEditor.enhance_image(self.fern2_img, self.monitor[1] / HEIGHT)
                    self.fs_btn_clicked(self.fern2, new_image, 450, 598)

                    self.player.fs_update(600, 500, self.fullscreen, self.monitor[1] / HEIGHT)


                elif ((event.type == pygame.KEYDOWN and event.scancode == 41) or
                      self.fs_btn.is_clicked(event)) and self.fullscreen:
                    self.fullscreen = False
                    self.screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)

                    self.fs_btn_clicked(self.bckgnd, self.bckgnd_img, 0, 0)
                    self.fs_btn_clicked(self.border, self.border_img, 0, 0)

                    fs_btn_img = ImgEditor.load_image("fs_btn_night_1.png", f"\main_menu", -1)
                    self.fs_btn_clicked(self.fs_btn, fs_btn_img, self.bckgnd.rect[2] - 50, 25)

                    self.fs_btn_clicked(self.tree, self.tree_img, 271, 168)
                    self.fs_btn_clicked(self.mushroom, self.mushroom_img, 470, 140)
                    self.fs_btn_clicked(self.bush1, self.bush_img, 175, 92)
                    self.fs_btn_clicked(self.bush2, self.bush_img, 442, 370)
                    self.fs_btn_clicked(self.john, self.john_img, 435, 245)
                    self.fs_btn_clicked(self.fern1, self.fern1_img, 85, 303)
                    self.fs_btn_clicked(self.fern2, self.fern2_img, 165, 345)

                    self.player.fs_update(300, 300, self.fullscreen, self.monitor[1] / HEIGHT)

                if self.player.is_collide(self.john) and (event.type == pygame.KEYDOWN and event.scancode == 8):
                    self.john_dialog = True
                if (self.john.dialog.is_clicked(event) or (event.type == pygame.KEYDOWN and (
                        event.scancode == 79 or event.scancode == 7))) and self.john_dialog:
                    self.jack_dialog = False
                    self.running = False
                    return 4, self.fullscreen

            self.draw_scene()
            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(FPS)

    def fs_btn_clicked(self, sprite, image, x, y):
        sprite.image = image
        sprite.mask = pygame.mask.from_surface(image)
        sprite.rect = sprite.image.get_rect()
        sprite.rect.x = x
        sprite.rect.y = y

    def new_sprite(self, sprite, image, x, y):
        sprite.image = image
        sprite.rect = image.get_rect()
        sprite.rect.x = x
        sprite.rect.y = y
        sprite.mask = pygame.mask.from_surface(sprite.image)

    def draw_scene(self):

        self.visible_sprites.draw(self.screen)
        self.buttons.draw(self.screen)
        if self.john_dialog:
            self.john.draw_dialog(self.fullscreen, self.screen, self.monitor)
        else:
            self.visible_sprites.update(self.fullscreen, self.monitor[1] / HEIGHT)
