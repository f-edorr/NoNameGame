import os
import sys
import pygame

SIZE = WIDTH, HEIGHT = 700, 500


class ImgEditor():

    def load_image(self, name, path="", colorkey=None):
        fullname = os.path.join('data' + path, name)
        # если файл не существует, то выходим
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()

        image = pygame.image.load(fullname)
        if colorkey is not None:
            image = image.convert()
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        return image

    def enhance_image(self, img, val):
        return pygame.transform.scale(img, (WIDTH * val, HEIGHT * val))

    def cut_image(self, name):
        pass
