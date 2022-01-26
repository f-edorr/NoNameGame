import pygame
from Img_Editor import ImgEditor


class Character(pygame.sprite.Sprite):
    def __init__(self, sheet, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.columns = self.rows = 4
        self.sheet = sheet
        self.rect = pygame.Rect(0, 0, self.sheet.get_width() // self.columns,
                                self.sheet.get_height() // self.rows)
        self.cur_frame = 0
        self.frames = []
        self.frames = ImgEditor.cut_sheet(self.sheet, self.columns, self.rows)
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def fs_update(self, sheet, x, y):
        self.x, self.y = x, y
        self.sheet = sheet
        self.rect = pygame.Rect(0, 0, self.sheet.get_width() // self.columns,
                                self.sheet.get_height() // self.rows)
        self.frames = ImgEditor.cut_sheet(self.sheet, self.columns, self.rows)
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(self.x, self.y)

    def moving(self, direction):
        if direction == 's':
            self.cur_frame = (self.cur_frame + 1) % 4
            self.image = self.frames[self.cur_frame]
            self.rect.y += 5
        if direction == 'w':
            self.cur_frame = (self.cur_frame + 1) % 4 + 4
            self.image = self.frames[self.cur_frame]
            self.rect.y -= 5
        if direction == 'd':
            self.cur_frame = (self.cur_frame + 1) % 4 + 8
            self.image = self.frames[self.cur_frame]
            self.rect.x += 5
        if direction == 'a':
            self.cur_frame = (self.cur_frame + 1) % 4 + 12
            self.image = self.frames[self.cur_frame]
            self.rect.x -= 5


