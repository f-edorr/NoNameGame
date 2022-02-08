import pygame
from Img_Editor import ImgEditor
from main_menu import MainMenu
from scene import Scene

SIZE = WIDTH, HEIGHT = 700, 500
FPS = 60

if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('NoNameGame')
    monitor = [pygame.display.Info().current_w, pygame.display.Info().current_h]
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_icon(ImgEditor.load_image("icon.png", colorkey=-1))
    stage = 0, 0
    clock = pygame.time.Clock()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(pygame.Color('black'))

        if stage[0] == -1:
            running = False
        elif stage[0] == 0:
            menu = MainMenu(monitor)
            stage = menu.run()
        elif stage[0] == 1:
            first_scene = Scene(monitor, stage[1])
            stage = first_scene.run()

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
