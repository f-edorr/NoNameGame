import pygame

from player import Player
from Img_Editor import ImgEditor
from button import Button
from world_sprite import WorldSprite

SIZE = WIDTH, HEIGHT = 700, 500
FPS = 60

class Dialogue:
    def __init__(self, big_image, text, time):
        super().__init__()
        self.text = text
        self.big_image = big_image

        self.dialog_sprites = pygame.sprite.Group()
        if time == 'day':
            self.dialog_img = ImgEditor.enhance_image(ImgEditor.load_image("dialog_day.png", ""), 2)
        else:
            self.dialog_img = ImgEditor.enhance_image(ImgEditor.load_image("dialog_night.png", ""), 2)

        self.dialog = Button(self.dialog_img, 0, 350)
        self.big_sprite = pygame.sprite.Sprite()
        self.big_sprite.image = self.big_image
        self.big_sprite.rect = self.big_image.get_rect()
        self.big_sprite.rect.x = 450
        self.big_sprite.rect.y = 140
        self.dialog_sprites.add(self.big_sprite, self.dialog)

    def draw_dialog(self, fs, screen, monitor):
        keys = pygame.key.get_pressed()

        if fs:
            self.dialog.image = ImgEditor.enhance_image(self.dialog_img, monitor[1] / HEIGHT)
            self.dialog.rect = self.dialog.image.get_rect()
            self.dialog.rect.x = (monitor[0] - WIDTH * (monitor[1] / HEIGHT)) // 2
            self.dialog.rect.y = 668

            self.big_sprite.image = ImgEditor.enhance_image(self.big_image, monitor[1] / HEIGHT)
            self.big_sprite.rect = self.big_sprite.image.get_rect()
            self.big_sprite.rect.x = 900
            self.big_sprite.rect.y = 240
        else:
            self.dialog.image = self.dialog_img
            self.dialog.rect = self.dialog.image.get_rect()
            self.dialog.rect.x = 0
            self.dialog.rect.y = 386

            self.big_sprite.image = self.big_image
            self.big_sprite.rect = self.big_sprite.image.get_rect()
            self.big_sprite.rect.x = 450
            self.big_sprite.rect.y = 140

        self.dialog_sprites.draw(screen)
