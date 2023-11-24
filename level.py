from player import Player
from player_interface import Interface
from animation import Animation
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

            self.objects.append(player_object)

            UI = Interface()

            self.display.fill((100, 150, 200)) # это надо переделать я пока чисто для теста это добавил



            game_over = False

            while True:
                if not(player_object.GetAlive()):
                    game_over = True
                    break
                # здесь сперва будет происходить пересчет всяких физических событий, в том числе пересчет коллизий
                CheckCollisions(self)

                # потом будет происходить отрисовка
                for obj in self.objects:
                    self.display.blit(obj.GetSprite(), obj.GetRect())
                    continue


                pygame.display.update()
                # потом будет происходить обработка действий игрока
                UI.CheckUIClick()


                self.clock.tick(10)
                continue
            if not(game_over):
                break