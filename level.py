import time

from player import Player
from player_interface import Interface
from animation import Animation
from object import Object
import sys

import pygame
class Level:
    def __init__(self, objects, display, clock):
        self.objects = objects
        self.display = display
        self.clock = clock
        self.angle = 0

    def Play(self):
        while True:
            def CalcPhysics():
                self.objects[0].SetStand(False)
                self.objects[0].collide_on_side = False
                for i in range(1, len(self.objects)):
                    player_coord = self.objects[0].GetCoord()
                    player_size = self.objects[0].GetSize()
                    object_coord = self.objects[i].GetCoord()
                    object_size = self.objects[i].GetSize()



                    if abs(player_coord[0] - object_coord[0]) <= player_size[0]/2 + object_size[0]/2 and abs(player_coord[1] - object_coord[1]) <= player_size[1]/2 + object_size[1]/2:
                        self.objects[0].ResetXVelocity()
                        if player_coord[1] <= object_coord[1]:
                            self.objects[0].SetStand(True)
                        if player_coord[1] > object_coord[1]:
                            self.objects[0].ResetYVelocity()


            def CalcAngle(rotation):
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

            platform_sprite = Animation([pygame.image.load("cube2.png")])

            platform_coords = ((0, 688), (32, 688), (64, 688), (96, 688), (128, 688), (160, 688), (192, 688), (224, 688), (256, 688), (288, 688), (320, 688), (352, 688), (384, 688), (416, 688), (448, 688), (480, 688), (512, 688), (544, 688), (576, 688), (608, 688), (640, 688), (672, 688), (704, 688),
            (200, 600), (232, 600), (600, 520), (600, 552), (568, 410)) # пол и пара висящих платформ

            for platform in platform_coords:
                self.objects.append(Object(platform[0], platform[1], 32, 32, False, platform_sprite))
            

            game_over = False

            run_start_time = 0
            fall_start_time = 0

            player_move = False
            player_move_right = False

            while True:
                if not(player_object.GetAlive()):
                    game_over = True
                    break

                self.display.fill((100, 150, 200))

                # здесь сперва будет происходить пересчет всяких физических событий, в том числе пересчет коллизий

                CalcPhysics()
                # потом будет происходить отрисовка
                for obj in self.objects:
                    obj.Draw(self.display)

                player_jump = False

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_e:
                            CalcAngle(90)
                        if event.key == pygame.K_q:
                            CalcAngle(-90)
                        if event.key == pygame.K_a:
                            run_start_time = 0
                            player_move = False
                            player_move_right = False
                        if event.key == pygame.K_d:
                            run_start_time = 0
                            player_move = False
                            player_move_right = False
                        if event.key == pygame.K_SPACE:
                            player_jump = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            run_start_time = time.time()
                            player_move = True
                        if event.key == pygame.K_d:
                            player_move = True
                            run_start_time = time.time()
                            player_move_right = True

                if player_object.GetStand():
                    fall_start_time = 0
                    player_object.ResetYVelocity()
                else:
                    if fall_start_time == 0:
                        fall_start_time = time.time()
                    player_object.Falling(time.time() - fall_start_time)



                if player_object.collide_os_side == True:
                    run_start_time = time.time()

                if player_move:
                    player_object.SetMoveVelocity(time.time() - run_start_time)
                    player_object.MoveX(player_move_right)
                if player_jump and player_object.GetStand():
                    player_object.Jump()
                player_object.MoveY()



                #player_object.x = pygame.mouse.get_pos()[0]
                #player_object.y = pygame.mouse.get_pos()[1]




                self.display.blit(pygame.transform.rotate(self.display, self.angle), (0,0)) #вертит экран на заданный угол
                pygame.display.update()

                # потом будет происходить обработка действий игрока
                UI.CheckUIClick()

                self.clock.tick(400)
                continue
            if not(game_over):
                break