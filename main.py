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

# Draw the snake
def draw_snake(block_size, snake_body):
  for i, block in enumerate(snake_body):
    color = red if i == len(snake_body) - 1 else black
    pygame.draw.rect(screen, color, [block[0], block[1], block_size, block_size])

# Display score
def display_score(score):
  font = pygame.font.SysFont("comicsanms", 50)
  score_text = font.render(f"Score : {score}", True, red)
  screen.blit(score_text, [0, 0])