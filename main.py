import pygame
from level import Level
from animation import Animation
from object import Object
import sys

W = 1080
H = 720

clock = pygame.time.Clock()
display = pygame.display.set_mode((W, H))


# some_animation = Animation([pygame.image.load("cube.png"), pygame.image.load("cube2.png")])
# some_cube = Object(0,0,32,32,False,some_animation)
# first_level_objects = [some_cube]
entities = []
entities.append(Object(500, 500, 32, 32, Animation([pygame.image.load("cube.png")])))

Level1 = Level(entities, display, clock)
Level1.Play()