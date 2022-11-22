import pygame
import random
import snake

# COLORS
GREEN = (154, 205, 50)
RED = (220, 20, 60)

# SIZE
SIZE = width, height = 400, 400

# Game init
pygame.init()
surface = pygame.display.set_mode(SIZE)
snake = snake.Snake()

pygame.draw.rect(surface, GREEN, pygame.Rect(snake.x_init, snake.y_init, 20, 20))

x_fruit = random.randint(1, 400)
y_fruit = random.randint(1, 400)
pygame.draw.circle(surface, RED, (x_fruit, y_fruit), 10)

running = True
while running:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
