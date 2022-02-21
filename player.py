import pygame
from Img_Editor import ImgEditor

SIZE = WIDTH, HEIGHT = 700, 500


class Player(pygame.sprite.Sprite):
    def __init__(self, sheet, x, y, obstacles):
        super().__init__()
        self.direction = pygame.math.Vector2()
        self.speed = 2
        self.obstacles = obstacles

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

    def is_collide(self, sprite):
        self.rect.x += 3
        if pygame.sprite.collide_rect(self, sprite):
            self.rect.x -= 3
            return True
        self.rect.x -= 3

        self.rect.x -= 3
        if pygame.sprite.collide_rect(self, sprite):
            self.rect.x += 3
            return True
        self.rect.x += 3

        self.rect.y += 3
        if pygame.sprite.collide_rect(self, sprite):
            self.rect.y -= 3
            return True
        self.rect.y -= 3

        self.rect.y -= 3
        if pygame.sprite.collide_rect(self, sprite):
            self.rect.y += 3
            return True
        self.rect.y += 3

        return False

    def fs_update(self, sheet, x, y):
        self.x, self.y = x, y
        self.sheet = sheet
        self.rect = pygame.Rect(0, 0, self.sheet.get_width() // self.columns,
                                self.sheet.get_height() // self.rows)
        self.frames = ImgEditor.cut_sheet(self.sheet, self.columns, self.rows)
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(self.x, self.y)
        self.mask = pygame.mask.from_surface(self.image)

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def moving(self, speed):
        # if self.direction.magnitude() != 0:
        #    self.direction = self.direction.normalize()

        self.rect.x += speed * self.direction.x
        self.collision("h", speed)
        self.rect.y += speed * self.direction.y
        self.collision("v", speed)

    def collision(self, direction, speed):
        if direction == "h":
            for sprite in self.obstacles:
                if pygame.sprite.collide_mask(self, sprite):
                    self.rect.x -= speed * self.direction.x
        if direction == "v":
            for sprite in self.obstacles:
                if pygame.sprite.collide_mask(self, sprite):
                    self.rect.y -= speed * self.direction.y

    def update(self, fs, k):
        self.input()
        if fs:
            self.moving(int(self.speed * k))
        else:
            self.moving(self.speed)
