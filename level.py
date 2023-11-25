from player import Player
from player_interface import Interface
from animation import Animation
from object import Object

import pygame
class Level:
    def __init__(self, objects, display, clock):
        self.objects = objects
        self.display = display
        self.clock = clock

    def Play(self):
        while True:
            def CheckCollisions(self):
                # Короче не совсем знаю как нам лучше написать эту часть тк тут вероятно нам придется смотреть коллизии всех обьектов с любым другим обьектом, что звучит не очень
                return
            def Flip():
                return

            player_sprite = Animation([pygame.image.load("cube.png")])
            player_object = Player(100, 100, 32, 32, player_sprite)

            UI = Interface()

            self.display.fill((100, 150, 200)) # это надо переделать я пока чисто для теста это добавил

            platform_sprite = Animation([pygame.image.load("./sprites/base_platform.png")])

            platform_coords = ((0, 656), (64, 656), (128, 656), (192, 656), (256, 656), (320, 656), (384, 656), (448, 656), (512, 656), (576, 656), (640, 656), (704, 656), (768, 656), (832, 656), (896, 656), (960, 656), (1024, 656), (1088, 656),
            (200, 600), (264, 600), (460, 520), (524, 520))

            for platform in platform_coords:
                self.objects.append(Object(platform[0], platform[1], 64, 64, False, platform_sprite))

            game_over = False

            while True:
                if not(player_object.GetAlive()):
                    game_over = True
                    break
                # здесь сперва будет происходить пересчет всяких физических событий, в том числе пересчет коллизий
                CheckCollisions(self)

                # потом будет происходить отрисовка
                for obj in self.objects:
                    obj.Draw(self.display)
                    # self.display.blit(obj.GetSprite(), obj.GetRect())
                    continue


                pygame.display.update()
                # потом будет происходить обработка действий игрока
                UI.CheckUIClick()


                self.clock.tick(10)
                continue
            if not(game_over):
                break