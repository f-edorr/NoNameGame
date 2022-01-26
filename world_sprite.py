import pygame
from Img_Editor import ImgEditor
from button import Button

SIZE = WIDTH, HEIGHT = 700, 500


class WorldSprite(pygame.sprite.Sprite):
    def __init__(self, img, x, y, text="Здесь ничего нет.", big_image=-1):
        super().__init__()
        self.image = img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.text = text
        self.big_image = big_image

        self.dialog_sprites = pygame.sprite.Group()

        self.dialog_img = ImgEditor.enhance_image(ImgEditor.load_image("dialog.png", ""), 2)
        self.dialog = Button(self.dialog_img, 0, 350)
        if self.big_image != -1:
            self.big_sprite = pygame.sprite.Sprite()
            self.big_sprite.image = self.big_image
            self.big_sprite.rect = self.big_image.get_rect()
            self.big_sprite.rect.x = 500
            self.big_sprite.rect.y = 140
            self.dialog_sprites.add(self.big_sprite)

        self.dialog_sprites.add(self.dialog)

    def draw_dialog(self, fs, screen, monitor):
        if fs:
            self.dialog.image = ImgEditor.enhance_image(self.dialog_img, monitor[1] / HEIGHT)
            self.dialog.rect = self.dialog.image.get_rect()
            self.dialog.rect.x = (monitor[0] - WIDTH*(monitor[1] / HEIGHT))//2
            self.dialog.rect.y = 668

            self.big_sprite.image = ImgEditor.enhance_image(self.big_image, monitor[1] / HEIGHT)
            self.big_sprite.rect = self.big_sprite.image.get_rect()
            self.big_sprite.rect.x = 1000
            self.big_sprite.rect.y = 240
        else:
            self.dialog.image = self.dialog_img
            self.dialog.rect = self.dialog.image.get_rect()
            self.dialog.rect.x = 0
            self.dialog.rect.y = 386

            self.big_sprite.image = self.big_image
            self.big_sprite.rect = self.big_sprite.image.get_rect()
            self.big_sprite.rect.x = 500
            self.big_sprite.rect.y = 140

        self.dialog_sprites.draw(screen)
