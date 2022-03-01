import pygame
from random import randrange

from enemy import Enemy
from player import Player
from Img_Editor import ImgEditor
from button import Button

SIZE = WIDTH, HEIGHT = 700, 500
FPS = 60


class Level:
    def __init__(self, monitor, parent_fs, params_filename):
        self.params_filename = params_filename
        file = open(f"./data/txts/{self.params_filename}.txt", encoding="utf-8")
        data = file.read().split('\n')
        file.close()
        self.time = data[0]
        self.enemies_cnt = int(data[1])
        self.enemies_cnt_onField = int(data[2])
        self.enemies_attack = int(data[3])
        self.enemy_img = data[4]
        self.enemy_bullet_img = data[5]
        self.enemy_dir = 0
        self.next_step = int(data[6])

        self.monitor = monitor
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.running = True
        self.fullscreen = False
        self.parent_fs = parent_fs

        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.buttons = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.onField_enemies = 0
        self.bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.border_gr = pygame.sprite.Group()

        self.bckgnd = pygame.sprite.Sprite()
        self.border = pygame.sprite.Sprite()
        if self.time == 'd':
            self.fs_btn_img = ImgEditor.load_image("fs_btn_day_1.png", f"\main_menu", -1)
            self.bckgnd_img = ImgEditor.enhance_image(ImgEditor.load_image("bck_day.png", f"\level"), 2)
            self.border_img = ImgEditor.enhance_image(
                ImgEditor.load_image("border_day.png", f"\level", (255, 255, 255)), 2)
        elif self.time == 'n':
            self.fs_btn_img = ImgEditor.load_image("fs_btn_night_1.png", f"\main_menu", -1)
            self.bckgnd_img = ImgEditor.enhance_image(ImgEditor.load_image("bck_night.png", f"\level"), 2)
            self.border_img = ImgEditor.enhance_image(
                ImgEditor.load_image("border_night.png", f"\level", (255, 255, 255)), 2)
        else:
            print('txt file error')

        self.new_sprite(self.bckgnd, self.bckgnd_img, 0, 0)
        self.new_sprite(self.border, self.border_img, 0, 0)
        self.border.mask = pygame.mask.from_surface(self.border_img)

        self.player = Player(self.border.rect.x + self.border.rect.width // 2,
                             self.border.rect.y + self.border.rect.height // 2, self.obstacle_sprites)

        self.fs_btn = Button(self.fs_btn_img, self.bckgnd.rect[2] - 50, 25)

        self.buttons.add(self.fs_btn)
        self.visible_sprites.add(self.bckgnd, self.player)
        self.border_gr.add(self.border)
        self.obstacle_sprites.add(self.border)

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

                    for bullet in self.bullets:
                        bullet.kill()

                    for bullet in self.enemy_bullets:
                        bullet.kill()

                    for enemy in self.enemies:
                        enemy.kill()

                    self.onField_enemies = 0

                    new_image = ImgEditor.enhance_image(self.bckgnd_img, self.monitor[1] / HEIGHT)
                    self.fs_btn_clicked(self.bckgnd, new_image,
                                        (self.monitor[0] - WIDTH * (self.monitor[1] / HEIGHT)) // 2, 0)

                    new_image = ImgEditor.enhance_image(self.border_img, self.monitor[1] / HEIGHT)
                    self.fs_btn_clicked(self.border, new_image,
                                        (self.monitor[0] - WIDTH * (self.monitor[1] / HEIGHT)) // 2, 0)
                    if self.time == 'd':
                        new_image = ImgEditor.enhance_image(ImgEditor.load_image("fs_btn_day_2.png", f"\main_menu", -1),
                                                            self.monitor[1] / HEIGHT)
                    else:
                        new_image = ImgEditor.enhance_image(
                            ImgEditor.load_image("fs_btn_night_2.png", f"\main_menu", -1),
                            self.monitor[1] / HEIGHT)
                    self.fs_btn_clicked(self.fs_btn, new_image,
                                        self.monitor[0] - 25 - new_image.get_width() - (
                                                (self.monitor[0] - WIDTH * (self.monitor[1] / HEIGHT)) // 2), 25)

                    self.player.fs_update(self.border.rect.x + self.border.rect.width // 2,
                                          self.border.rect.y + self.border.rect.height // 2, self.fullscreen,
                                          self.monitor[1] / HEIGHT)

                elif ((event.type == pygame.KEYDOWN and event.scancode == 41) or
                      self.fs_btn.is_clicked(event)) and self.fullscreen:
                    self.fullscreen = False
                    self.screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)

                    for bullet in self.bullets:
                        bullet.kill()

                    for bullet in self.enemy_bullets:
                        bullet.kill()

                    for enemy in self.enemies:
                        enemy.kill()

                    self.onField_enemies = 0

                    self.fs_btn_clicked(self.bckgnd, self.bckgnd_img, 0, 0)
                    self.fs_btn_clicked(self.border, self.border_img, 0, 0)

                    if self.time == 'd':
                        fs_btn_img = ImgEditor.load_image("fs_btn_day_1.png", f"\main_menu", -1)
                    else:
                        fs_btn_img = ImgEditor.load_image("fs_btn_night_1.png", f"\main_menu", -1)
                    self.fs_btn_clicked(self.fs_btn, fs_btn_img, self.bckgnd.rect[2] - 50, 25)
                    self.player.fs_update(self.border.rect.x + self.border.rect.width // 2,
                                          self.border.rect.y + self.border.rect.height // 2, self.fullscreen,
                                          self.monitor[1] / HEIGHT)

                elif (event.type == pygame.KEYDOWN and event.scancode == 44):
                    self.bullets.add(self.player.attack(self.fullscreen, self.monitor[1] / HEIGHT))

                if self.enemies_cnt == 0:
                    self.running = False
                    return self.next_step, self.fullscreen

            for enemy in self.enemies:
                if enemy.dying(self.bullets):
                    self.enemies_cnt -= 1
                    self.onField_enemies -= 1
            self.enemy_spawn(self.fullscreen)
            self.draw_level()
            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(FPS)

    def draw_level(self):
        self.visible_sprites.draw(self.screen)
        self.enemies.draw(self.screen)
        self.bullets.draw(self.screen)
        self.border_gr.draw(self.screen)
        self.buttons.draw(self.screen)

        self.visible_sprites.update(self.fullscreen, self.monitor[1] / HEIGHT)
        self.bullets.update(self.fullscreen, self.monitor[1] / HEIGHT, self.border.rect)

    def enemy_spawn(self, fs):
        if self.onField_enemies < self.enemies_cnt_onField and self.enemies_cnt - self.onField_enemies > 0:
            if fs:
                if self.enemy_dir == 0:
                    enemy = Enemy(self.enemy_img, self.enemy_bullet_img, randrange(300, 900), randrange(300, 500), 1, 0,
                                  self.fullscreen, self.monitor[1] / HEIGHT)
                if self.enemy_dir == 1:
                    enemy = Enemy(self.enemy_img, self.enemy_bullet_img, randrange(300, 900), randrange(300, 600), 0, 1,
                                  self.fullscreen, self.monitor[1] / HEIGHT)
                if self.enemy_dir == 2:
                    enemy = Enemy(self.enemy_img, self.enemy_bullet_img, randrange(300, 900), randrange(300, 600), -1,
                                  0,
                                  self.fullscreen, self.monitor[1] / HEIGHT)
                if self.enemy_dir == 3:
                    enemy = Enemy(self.enemy_img, self.enemy_bullet_img, randrange(300, 900), randrange(300, 600), 0,
                                  -1,
                                  self.fullscreen, self.monitor[1] / HEIGHT)
            else:
                if self.enemy_dir == 0:
                    enemy = Enemy(self.enemy_img, self.enemy_bullet_img, randrange(100, 600), randrange(100, 400), 1, 0,
                                  self.fullscreen, self.monitor[1] / HEIGHT)
                if self.enemy_dir == 1:
                    enemy = Enemy(self.enemy_img, self.enemy_bullet_img, randrange(100, 600), randrange(100, 400), 0, 1,
                                  self.fullscreen, self.monitor[1] / HEIGHT)
                if self.enemy_dir == 2:
                    enemy = Enemy(self.enemy_img, self.enemy_bullet_img, randrange(100, 600), randrange(100, 400), -1,
                                  0,
                                  self.fullscreen, self.monitor[1] / HEIGHT)
                if self.enemy_dir == 3:
                    enemy = Enemy(self.enemy_img, self.enemy_bullet_img, randrange(100, 600), randrange(100, 400), 0,
                                  -1,
                                  self.fullscreen, self.monitor[1] / HEIGHT)

            self.enemies.add(enemy)
            self.obstacle_sprites.add(enemy)
            self.onField_enemies += 1

            self.enemy_dir += 1
            self.enemy_dir %= 4

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
