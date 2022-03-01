import pygame
from Img_Editor import ImgEditor
from bullet import Bullet

SIZE = WIDTH, HEIGHT = 700, 500


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, obstacles):
        super().__init__()
        self.direction = pygame.math.Vector2()
        self.speed = 2
        self.obstacles = obstacles

        self.x = x
        self.y = y

        self.image = ImgEditor.enhance_image(ImgEditor.load_image("down_idle.png", f"\player", -1), 2)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.fs_mode = False

        self.import_frames()
        self.status = 'down'
        self.frame = 0
        self.animation_speed = 0.15

        self.health_points = 100

        # self.mask = pygame.mask.from_surface(self.image)

    def import_frames(self):
        down = ImgEditor.enhance_image(ImgEditor.load_image("down_idle.png", f"\player", -1), 2)
        up = ImgEditor.enhance_image(ImgEditor.load_image("up_idle.png", f"\player", -1), 2)
        left = ImgEditor.enhance_image(ImgEditor.load_image("left_idle.png", f"\player", -1), 2)
        right = ImgEditor.enhance_image(ImgEditor.load_image("right_idle.png", f"\player", -1), 2)
        self.animations = {
            'down': [down, ImgEditor.enhance_image(ImgEditor.load_image("down1.png", f"\player", -1), 2), down,
                     ImgEditor.enhance_image(ImgEditor.load_image("down2.png", f"\player", -1), 2)],
            'up': [up, ImgEditor.enhance_image(ImgEditor.load_image("up1.png", f"\player", -1), 2), up,
                   ImgEditor.enhance_image(ImgEditor.load_image("up2.png", f"\player", -1), 2)],
            'left': [left, ImgEditor.enhance_image(ImgEditor.load_image("left1.png", f"\player", -1), 2), left,
                     ImgEditor.enhance_image(ImgEditor.load_image("left2.png", f"\player", -1), 2)],
            'right': [right, ImgEditor.enhance_image(ImgEditor.load_image("right1.png", f"\player", -1), 2), right,
                      ImgEditor.enhance_image(ImgEditor.load_image("right2.png", f"\player", -1), 2)],
            'down_idle': [down],
            'up_idle': [up],
            'left_idle': [left],
            'right_idle': [right]}

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

    def fs_update(self, x, y, fs, k):
        self.rect.x = self.x = x
        self.rect.y = self.y = y
        self.fs_mode = fs

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
            self.status = 'left'
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
            self.status = 'right'
        else:
            self.direction.x = 0

    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0 and not 'idle' in self.status:
            self.status = self.status + "_idle"

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

    def attack(self, fs, k):
        if fs:
            img = ImgEditor.enhance_image(ImgEditor.load_image("player_ball.png", f"\level", -1), 2 * k)
        else:
            img = ImgEditor.enhance_image(ImgEditor.load_image("player_ball.png", f"\level", -1), 2)
        bullet = Bullet(img, self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2, self.direction.x,
                        self.direction.y)
        return bullet

    def animate(self, k):
        animation = self.animations[self.status]

        self.frame += self.animation_speed
        if self.frame >= len(animation):
            self.frame = 0

        if self.fs_mode:
            self.image = ImgEditor.enhance_image(animation[int(self.frame)], k)
        else:
            self.image = animation[int(self.frame)]
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x, self.y)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, fs, k):
        self.input()
        self.get_status()
        self.animate(k)
        if fs:
            self.moving(int(self.speed * k))
        else:
            self.moving(self.speed)
        self.x, self.y = self.rect.x, self.rect.y
