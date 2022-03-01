import pygame
from Img_Editor import ImgEditor
from level import Level
from main_menu import MainMenu
from scene1 import Scene_1
from scene2 import Scene_2
from scene3 import Scene_3

SIZE = WIDTH, HEIGHT = 700, 500
FPS = 60

if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('NoNameGame')
    monitor = [pygame.display.Info().current_w, pygame.display.Info().current_h]
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_icon(ImgEditor.load_image("icon.png", colorkey=-1))
    stage = (0, 0)
    clock = pygame.time.Clock()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(pygame.Color('black'))
        print(stage[0])
        if stage[0] == -1:
            running = False
        elif stage[0] == 0:
            menu = MainMenu(monitor)
            stage = menu.run()
        elif stage[0] == 1:
            first_scene = Scene_1(monitor, stage[1])
            stage = first_scene.run()
        elif stage[0] == 2:
            first_lvl = Level(monitor, stage[1], 'lvl_1')
            stage = first_lvl.run()
        elif stage[0] == 3:
            second_scene = Scene_2(monitor, stage[1])
            stage = second_scene.run()
        elif stage[0] == 4:
            second_lvl = Level(monitor, stage[1], 'lvl_2')
            stage = second_lvl.run()
        elif stage[0] == 5:
            third_scene = Scene_3(monitor, stage[1])
            stage = third_scene.run()

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
