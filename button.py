import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def is_clicked(self):
        pass

    def update(self):
        pass
