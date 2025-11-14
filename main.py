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

def game_loop():
  x, y = width // 2, height // 2
  x_change, y_change = 0, 0

  # Initial snake body
  snake_body = []
  snake_length = 1

  # Random food position
  food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
  food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0

  # Main game loop
  game_over = False
  game_close = False

  while not game_over:
    # Movement keys
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        game_over  = True
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          x_change = 0
          y_change = -block_size
        elif event.key == pygame.K_DOWN:
          x_change = 0
          y_change = block_size
        elif event.key == pygame.K_LEFT:
          x_change = -block_size
          y_change = 0
        elif event.key == pygame.K_RIGHT:
          x_change = block_size
          y_change = 0

    # Check if the snake hits the wall
    if x >= width or x < 0 or y >= height or y < 0:
      game_close = True
      game_over = True

    # Update snake's head position
    x += x_change
    y += y_change
    screen.fill(blue)

    # Draw food
    pygame.draw.rect(screen, green, [food_x, food_y, block_size, block_size])

    # Update the snake's body
    snake_head = []
    snake_head.append(x)
    snake_head.append(y)
    snake_body.append(snake_head)

    if len(snake_body) > snake_length:
      del snake_body[0]

    # Check if the snake runs into itself
    for block in snake_body[:-1]:
      if block == snake_head:
        game_over = True

    draw_snake(block_size, snake_body)
    display_score(snake_length - 1)
    pygame.display.update()

    # Check if the snake eats food
    if x == food_x and y == food_y:
      food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
      food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0
      snake_length += 1

    clock.tick(snake_speed)

    while game_close:
      screen.fill(black)
      font = pygame.font.SysFont("comicsanms", 35)
      game_over_text = font.render("Game over! Press Q to Quit or C to Continue", True, red)
      screen.blit(game_over_text, [width // 15, height // 2.4])
      pygame.display.update()

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q:
            pygame.quit()
            quit()
          elif event.key == pygame.K_c:
            game_loop()
            return