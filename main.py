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
MOVEEVENT = pygame.USEREVENT+1
pygame.time.set_timer(MOVEEVENT, 500)
while not snake.lost:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]: snake.update_direction("up")
    if keys[pygame.K_DOWN]: snake.update_direction("down")
    if keys[pygame.K_LEFT]: snake.update_direction("left")
    if keys[pygame.K_d]: snake.update_direction("right")

    for event in pygame.event.get():
        if event.type == pygame.QUIT: snake.lost = True
        if event.type == MOVEEVENT:
            if snake.check_collisions(fruit):
                fruit.reset()
            snake.update_body()
            update_surface(surface, snake, fruit)
            pygame.display.flip()

print("You lost!")
