import pygame
from Img_Editor import ImgEditor

SIZE = WIDTH, HEIGHT = 700, 500


class Bullet(pygame.sprite.Sprite):
    def __init__(self, img, x, y, dirx, diry):
        super().__init__()
        self.direction = [1, 0]
        if not (dirx == 0 and diry == 0):
            self.direction = [dirx, diry]
        self.speed = 3
        self.x = x
        self.y = y

        self.image = img
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def fs_update(self, img):
        self.x, self.y = 0, 0
        self.image = img
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x, self.y)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, fs, k, border):
        if fs:
            self.rect.y += self.speed * k * self.direction[1]
            self.rect.x += self.speed * k * self.direction[0]
        else:
            self.rect.y += self.speed * self.direction[1]
            self.rect.x += self.speed * self.direction[0]

        if self.rect.x <= border.x or self.rect.x + self.rect.width >= border.x + border.width:
            self.kill()

        if self.rect.y <= border.y or self.rect.y + self.rect.height >= border.y + border.height:
            self.kill()
