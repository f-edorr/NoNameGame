import pygame
from Img_Editor import ImgEditor
from bullet import Bullet

SIZE = WIDTH, HEIGHT = 700, 500


class Enemy(pygame.sprite.Sprite):
    def __init__(self, img_name, bullet_img_name, x, y, dirx, diry, fs, k):
        super().__init__()
        self.speed = 2
        self.direction = [dirx, diry]

        self.x = x
        self.y = y
        self.img_name = img_name
        self.bullet_img_name = bullet_img_name

        if fs:
            self.image = ImgEditor.enhance_image(ImgEditor.load_image(f"{self.img_name}.png", f"\level", -1), 2 * k)
        else:
            self.image = ImgEditor.enhance_image(ImgEditor.load_image(f"{self.img_name}.png", f"\level", -1), 2)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def fs_update(self, fs, k):
        if fs:
            self.image = ImgEditor.enhance_image(ImgEditor.load_image(f"{self.img_name}.png", f"\level", -1), 2 * k)
        else:
            self.image = ImgEditor.enhance_image(ImgEditor.load_image(f"{self.img_name}.png", f"\level", -1), 2)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def moving(self, speed):
        self.rect.x += speed * self.direction.x
        self.rect.y += speed * self.direction.y

    def dying(self, bullets):
        for bullet in bullets:
            if pygame.sprite.collide_mask(self, bullet):
                self.kill()
                return True
        return False

    def attack(self, fs, k):
        if fs:
            if self.direction[0] == 1 and self.direction[1] == 0:
                img = ImgEditor.enhance_image(ImgEditor.load_image(f"{self.bullet_img_name}_right.png", f"\level", -1),
                                              2 * k)
            if self.direction[0] == -1 and self.direction[1] == 0:
                img = ImgEditor.enhance_image(ImgEditor.load_image(f"{self.bullet_img_name}_left.png", f"\level", -1),
                                              2 * k)
            if self.direction[0] == 0 and self.direction[1] == 1:
                img = ImgEditor.enhance_image(ImgEditor.load_image(f"{self.bullet_img_name}_down.png", f"\level", -1),
                                              2 * k)
            if self.direction[0] == 0 and self.direction[1] == -1:
                img = ImgEditor.enhance_image(ImgEditor.load_image(f"{self.bullet_img_name}_up.png", f"\level", -1),
                                              2 * k)
        else:
            if self.direction[0] == 1 and self.direction[1] == 0:
                img = ImgEditor.enhance_image(ImgEditor.load_image(f"{self.bullet_img_name}_right.png", f"\level", -1),
                                              2)
            if self.direction[0] == -1 and self.direction[1] == 0:
                img = ImgEditor.enhance_image(ImgEditor.load_image(f"{self.bullet_img_name}_left.png", f"\level", -1),
                                              2)
            if self.direction[0] == 0 and self.direction[1] == 1:
                img = ImgEditor.enhance_image(ImgEditor.load_image(f"{self.bullet_img_name}_down.png", f"\level", -1),
                                              2)
            if self.direction[0] == 0 and self.direction[1] == -1:
                img = ImgEditor.enhance_image(ImgEditor.load_image(f"{self.bullet_img_name}_up.png", f"\level", -1), 2)

        bullet = Bullet(img, self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2, self.direction[0],
                        self.direction[1])
        return bullet

    def update(self, fs, k):
        pass
