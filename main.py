import pygame
import random
import snake

GREEN = (154, 205, 50)
RED = (220, 20, 60)
SIZE = width, height = 400, 400


class Fruit:
    def __init__(self):
        self.x_fruit = random.randint(1, 380)
        self.y_fruit = random.randint(1, 380)
        while self.x_fruit % 20 != 0:
            self.x_fruit = random.randint(1, 380)
        while self.y_fruit % 20 != 0:
            self.y_fruit = random.randint(1, 380)
        self.x_fruit += 10
        self.y_fruit += 10

    def reset(self):
        self.x_fruit = random.randint(1, 380)
        while self.x_fruit % 20 != 0:
            self.x_fruit = random.randint(1, 380)
        self.y_fruit = random.randint(1, 380)
        while self.y_fruit % 20 != 0:
            self.y_fruit = random.randint(1, 380)
        self.x_fruit += 10
        self.y_fruit += 10


def update_surface(screen, snake, fruit):
    """
    Updates the screen everytime the snake moves.
    :param screen:
    :param snake:
    :return:
    """
    snake_body_rect_ = []
    screen.fill((0, 0, 0, 0))

    # fruit_rect_ = pygame.draw.rect(screen, RED, pygame.Rect(fruit.x_fruit, fruit.y_fruit, 20, 20))
    fruit_rect_ = pygame.draw.circle(surface, RED, (fruit.x_fruit, fruit.y_fruit), 15)

    for body in snake.body:
        snake_body_rect_.append(pygame.draw.rect(screen, GREEN, pygame.Rect(body[0], body[1], 20, 20)))
    snake_head_ = snake_body_rect_[0]
    snake_body_rect_.pop(0)
    return snake_head_, snake_body_rect_, fruit_rect_


def check_collisions_fruit(snake_head_, fruit_rect_):
    """
    Returns true if the snake head is touching the fruit.
    :param snake_head_:
    :param fruit_rect_:
    :return:
    """
    if pygame.Rect.colliderect(snake_head_, fruit_rect_):
        return True
    else:
        return False


def check_collisions_snake(snake_head_, snake_body_rect_):
    """
    Returns true if snake head is touching the snake body.
    :param snake_head_:
    :param snake_body_rect_:
    :return:
    """
    if pygame.Rect.collidelist(snake_head_, snake_body_rect_) != -1:
        return True
    else:
        return False


# Window init
pygame.init()
pygame.display.set_caption('~ Snake ~')
surface = pygame.display.set_mode(SIZE)
pygame.display.set_icon(pygame.image.load('icon.png'))

# Game init
snake = snake.Snake()
fruit = Fruit()
snake_head, snake_body_rect, fruit_rect = update_surface(surface, snake, fruit)

# Launch game
MOVEEVENT = pygame.USEREVENT + 1
pygame.time.set_timer(MOVEEVENT, 300)
while not snake.lost:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]: snake.update_direction("up")
    if keys[pygame.K_DOWN]: snake.update_direction("down")
    if keys[pygame.K_LEFT]: snake.update_direction("left")
    if keys[pygame.K_RIGHT]: snake.update_direction("right")

    for event in pygame.event.get():
        if event.type == pygame.QUIT or check_collisions_snake(snake_head, snake_body_rect):
            snake.lost = True
        if event.type == MOVEEVENT:
            if check_collisions_fruit(snake_head, fruit_rect):
                fruit.reset()
                snake.longer()
            snake.update_body()
            snake_head, snake_body_rect, fruit_rect = update_surface(surface, snake, fruit)
            pygame.display.flip()
print("You lost!")
