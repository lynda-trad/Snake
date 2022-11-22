import pygame
import random
import snake

GREEN = (154, 205, 50)
RED = (220, 20, 60)
SIZE = width, height = 400, 400


class Fruit:
    def __init__(self):
        self.x_fruit = random.randint(1, 400)
        self.y_fruit = random.randint(1, 400)

    def reset(self):
        self.x_fruit = random.randint(1, 400)
        self.y_fruit = random.randint(1, 400)


def update_surface(screen, snake, fruit):
    """
    Updates the screen everytime the snake moves.
    :param screen:
    :param snake:
    :return:
    """
    screen.fill((0, 0, 0, 0))
    for body in snake.body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(body[0], body[1], 20, 20))

    pygame.draw.circle(surface, RED, (fruit.x_fruit, fruit.y_fruit), 10)


# Window init
pygame.init()
pygame.display.set_caption('~ Snake ~')
surface = pygame.display.set_mode(SIZE)
pygame.display.set_icon(pygame.image.load('icon.png'))

# Game init
snake = snake.Snake()
fruit = Fruit()

# Launch game
clock = pygame.time.Clock()
time_elapsed_since_last_action = 0
while not snake.lost:
    dt = clock.tick()
    time_elapsed_since_last_action += dt
    if time_elapsed_since_last_action > 50:
        for event in pygame.event.get():
            snake.update_body()
            if snake.check_collisions(fruit):
                fruit.reset()
            update_surface(surface, snake, fruit)
            pygame.display.flip()
            if event.type == pygame.QUIT:
                snake.lost = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.update_direction("up")
                if event.key == pygame.K_DOWN:
                    snake.update_direction("down")
                if event.key == pygame.K_LEFT:
                    snake.update_direction("left")
                if event.key == pygame.K_RIGHT:
                    snake.update_direction("right")

print("You lost!")
