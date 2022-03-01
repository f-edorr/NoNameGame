import pygame
from Img_Editor import ImgEditor
from button import Button

SIZE = WIDTH, HEIGHT = 700, 500


class WorldSprite(pygame.sprite.Sprite):
    def __init__(self, img, x, y, text='', big_image=-1, time='day'):
        super().__init__()
        self.image = img
        self.time = time
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.text = text
        self.big_image = big_image

        self.dialog_sprites = pygame.sprite.Group()

        self.dialog_img = ImgEditor.enhance_image(ImgEditor.load_image(f"dialog_{time}.png", ""), 2)
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
        keys = pygame.key.get_pressed()
        self.screen = pygame.display.get_surface()
        if fs:
            self.dialog.image = ImgEditor.enhance_image(self.dialog_img, monitor[1] / HEIGHT)
            self.dialog.rect = self.dialog.image.get_rect()
            self.dialog.rect.x = (monitor[0] - WIDTH * (monitor[1] / HEIGHT)) // 2
            self.dialog.rect.y = 668

            self.big_sprite.image = ImgEditor.enhance_image(self.big_image, monitor[1] / HEIGHT)
            self.big_sprite.rect = self.big_sprite.image.get_rect()
            self.big_sprite.rect.x = 900
            self.big_sprite.rect.y = 240
            self.dialog_sprites.draw(screen)

            font = pygame.font.SysFont('Comic Sans MS', 30)
            if self.time == 'day':
                text = self.text.split('\n')
                for i in range(len(text)):
                    self.screen.blit(font.render(text[i], False, (159, 88, 68)),
                                     (self.dialog.rect.x + 100, self.dialog.rect.y + 30 + 40 * i))
            else:
                text = self.text.split('\n')
                for i in range(len(text)):
                    self.screen.blit(font.render(text[i], False, (47, 29, 113)),
                                     (self.dialog.rect.x + 100, self.dialog.rect.y + 30 + 40 * i))
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
            font = pygame.font.SysFont('Comic Sans MS', 20)
            if self.time == 'day':

                text = self.text.split('\n')
                print(text)
                for i in range(len(text)):
                    self.screen.blit(font.render(text[i], False, (159, 88, 68)),
                                     (self.dialog.rect.x + 50, self.dialog.rect.y + 15 + 20 * i))
            else:
                text = self.text.split('\n')
                for i in range(len(text)):
                    self.screen.blit(font.render(text[i], False, (47, 29, 113)),
                                     (self.dialog.rect.x + 50, self.dialog.rect.y + 15 + 20 * i))
