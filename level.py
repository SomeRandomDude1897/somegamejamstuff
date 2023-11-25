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

            player_sprite = Animation([pygame.image.load("cube.png"), pygame.image.load("cube2.png")])
            player_object = Player(300, 350, 32, 32, 0, player_sprite)


            UI = Interface()



            game_over = False

            while True:
                if not(player_object.GetAlive()):
                    game_over = True
                    break
                # здесь сперва будет происходить пересчет всяких физических событий, в том числе пересчет коллизий

                # потом будет происходить отрисовка
                self.display.fill((100, 150, 200)) 
                for obj in self.objects:
                    obj.MoveObj()
                    player_object.collide(obj)
                    self.display.blit(obj.GetSprite(), (obj.rect.x, obj.rect.y))
                    continue
                
                self.display.blit(player_object.GetSprite(), (player_object.rect.x, player_object.rect.y))

                pygame.display.update()
                # потом будет происходить обработка действий игрока
                UI.CheckUIClick()


                self.clock.tick(10)
                continue
            if game_over:
                break