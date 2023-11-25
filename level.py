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
        self.angle = 0
        self.collided = False

    def Play(self):
        while True:
            """коллизии. проверяем только пары (игрок, другой объкт). игрок лежит в списке первым"""
            def CheckCollisions(self):

                player = self.objects[0]
                if player.rect.right >= 720 or player.rect.left <= 0:
                    self.objects[0].x_velocity = 0

                for i in range(1, len(self.objects)):
                    if (player.GetRect()).colliderect(self.objects[i].GetRect()):
                        if self.objects[i].is_threat:
                            game_over = True
                        # else:
                            # if self.objects[0].x_velocity > 0: # если движется вправо
                            #     self.objects[0].rect.right = self.objects[i].rect.left # то не движется вправо

                            # if self.objects[0].y_velocity < 0:
                            #     self.objects[0].ResetYVelocity()
                            #     self.collided = True

                            # if self.objects[0].y_velocity > 0:
                            #     self.objects[0].ResetYVelocity()
                # if xvel > 0:                      # если движется вправо
                #     self.rect.right = p.rect.left # то не движется вправо

                # if xvel < 0:                      # если движется влево
                #     self.rect.left = p.rect.right # то не движется влево

            # def Flip():
            #     return


            def CalcAngle(self, rotation):
                if self.angle + rotation > 271:
                    self.angle = 0
                elif self.angle + rotation < 0:
                    self.angle = 270
                else:
                    self.angle += rotation
                


            player_sprite = Animation([pygame.image.load("cube.png")])
            player_object = Player(100, 100, 32, 32, player_sprite)
            self.objects.append(player_object) 

            UI = Interface()

            self.display.fill((100, 150, 200)) # это надо переделать я пока чисто для теста это добавил

            platform_sprite = Animation([pygame.image.load("./sprites/base_platform.png")])

            platform_coords = ((0, 688), (32, 688), (64, 688), (96, 688), (128, 688), (160, 688), (192, 688), (224, 688), (256, 688), (288, 688), (320, 688), (352, 688), (384, 688), (416, 688), (448, 688), (480, 688), (512, 688), (544, 688), (576, 688), (608, 688), (640, 688), (672, 688), (704, 688),
            (200, 600), (232, 600), (600, 520), (600, 552), (568, 410)) # пол и пара висящих платформ

            for platform in platform_coords:
                self.objects.append(Object(platform[0], platform[1], 64, 64, False, platform_sprite))
            

            game_over = False

            while True:
                if not(player_object.GetAlive()):
                    game_over = True
                    break

                self.display.fill((100, 150, 200))

                # здесь сперва будет происходить пересчет всяких физических событий, в том числе пересчет коллизий

                # потом будет происходить отрисовка
                for obj in self.objects:
                    obj.Draw(self.display)
                    continue
                if not (self.collided):
                    player_object.Fall()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                keys = pygame.key.get_pressed()

                if keys[pygame.K_a]:
                    player_object.left = True
                if keys[pygame.K_d]:
                    player_object.right = True
                if keys[pygame.K_SPACE]:
                    player_object.Jump()
                if keys[pygame.K_e]:
                    CalcAngle(self, 90) 
                if keys[pygame.K_q]:
                    CalcAngle(self, -90)
                
                player_object.Move()
                CheckCollisions(self)
                player_object.SetFalse()

                player_object.base_y_velocity+=1

                self.display.blit(pygame.transform.rotate(self.display, self.angle), (0,0)) #вертит экран на заданный угол
                pygame.display.update()

                player_object.UpdateRect()

                # потом будет происходить обработка действий игрока
                UI.CheckUIClick()

                self.clock.tick(30)
                continue
            if not(game_over):
                break