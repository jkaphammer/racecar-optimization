import pygame
import numpy as np
from scipy import interpolate, spatial
import networkx as nx
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt

print("Success")

pygame.init()
screenWidth = 720
screenHeight = 720
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()
running = True
caption = pygame.display.set_caption('AI Racecar')

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("darkgreen")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
