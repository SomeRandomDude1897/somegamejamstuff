import pygame
from level import Level
from animation import Animation
from object import Object
from moving_object import MovingObject
import sys

W = 720
H = 720

clock = pygame.time.Clock()
display = pygame.display.set_mode((W, H))


# some_animation = Animation([pygame.image.load("cube.png"), pygame.image.load("cube2.png")])
# some_cube = Object(0,0,32,32,False,some_animation)
# first_level_objects = [some_cube]
entities = []
block = pygame.Surface((60, 60))
block.fill((50, 50, 50))
block = MovingObject(500, 500, 32, 32, Animation([block]), 80, 80)

entities.append(block)

Level1 = Level(entities, display, clock)
Level1.Play()