import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and (
                self.rect.x + self.rect[2]) >= event.pos[0] >= self.rect.x and (
                self.rect.y + self.rect[3]) >= event.pos[1] >= self.rect.y:
            return True
        else:
            return False

    def is_mouse_on(self):
        pos_x = pygame.mouse.get_pos()[0]
        pos_y = pygame.mouse.get_pos()[1]
        if self.rect.x + self.rect[2] >= pos_x >= self.rect.x and self.rect.y + self.rect[2] >= pos_y >= self.rect.y:
            return True
        else:
            return False

    def update(self):
        pass
