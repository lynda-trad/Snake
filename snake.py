class Snake:
    def __init__(self):
        self.x_init = 120
        self.y_init = 120
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

    def longer(self):
        """
        When the snake eats a fruit, it gets longer.
        :return:
        """
        self.body.append(self.body[-1])

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
            self.body[0] = (x_head + SIZE, y_head)

        # Snake is out of bounds
        if -20 in self.get_head_coordinates() or 400 in self.get_head_coordinates():
            self.lost = True
