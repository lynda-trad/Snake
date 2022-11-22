class Snake:
    def __init__(self):
        self.x_init = 100
        self.y_init = 100
        self.body = [(self.x_init, self.y_init)]
        self.direction = "right"
        self.lost = False

    def get_head_coordinates(self):
        """
        Returns snake's head coordinates.
        :return:
        """
        return self.body[0]

    def update_direction(self, dir):
        """
        Updates snake direction when arrow is pressed
        :param direction:
        :return:
        """
        self.direction = dir

    def update_body(self):
        """
        Depending on the snake direction, the body will be updated.
        :return:
        """
        SIZE = 20

        # Snake's body moves except for head
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i] = self.body[i - 1]

        # Head moves
        if self.direction == "up":
            x_head, y_head = self.get_head_coordinates()
            self.body[0] = (x_head, y_head - SIZE)

        if self.direction == "down":
            x_head, y_head = self.get_head_coordinates()
            self.body[0] = (x_head, y_head + SIZE)

        if self.direction == "left":
            x_head, y_head = self.get_head_coordinates()
            self.body[0] = (x_head - SIZE, y_head)

        if self.direction == "right":
            x_head, y_head = self.get_head_coordinates()
            self.body[0] = (x_head, y_head + SIZE)

        # Snake is out of bounds
        if -1 in self.get_head_coordinates() or 400 in self.get_head_coordinates():
            self.lost = True

    def check_collisions(self, fruit):
        """
        Returns true if snake collides fruit, false if not.
        :param fruit:
        :return: boolean
        """
        snake_X = self.get_head_coordinates()[0]
        snake_Y = self.get_head_coordinates()[1]
        if snake_X == fruit.x_fruit or snake_Y == fruit.y_fruit:
            return True
        else:
            return False
