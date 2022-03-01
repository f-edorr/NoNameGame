import os
import sys
import pygame


class ImgEditor:
    @staticmethod
    def load_image(name, path="", colorkey=None):
        fullname = os.path.join('data' + path, name)
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

    @staticmethod
    def enhance_image(img, val):
        return pygame.transform.scale(img, (img.get_rect()[2] * val, img.get_rect()[3] * val))

    @staticmethod
    def cut_sheet(sheet, columns, rows):
        frames = []
        rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                           sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (rect.w * i, rect.h * j)
                frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, rect.size)))

        return frames
