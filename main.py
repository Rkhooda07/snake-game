import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 600, 400

# Colors (RGB format)
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Create game window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake game by Rakshit Hooda')

#Clock and speed
clock = pygame.time.Clock()
snake_speed = 15

# Snake and food size
block_size = 10