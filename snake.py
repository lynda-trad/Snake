class Snake:
    def __init__(self):
        self.x_init = 199
        self.y_init = 199
        self.body = [(self.x_init, self.y_init)]
        self.direction = "down"
        self.lost = False

    def get_head_coordinates(self):
        return self.body[0]

    def update_direction(self, direction):
        self.direction = direction

    def update_body(self):
        """
        Depending on the snake direction, the body will be updated.
        :return:
        """
        # Snake's body moves except for head
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i] = self.body[i - 1]

        # Head moves
        if self.direction == "up":
            x_head, y_head = self.get_head_coordinates()
            self.body[0] = (x_head, y_head - 1)

        if self.direction == "down":
            x_head, y_head = self.get_head_coordinates()
            self.body[0] = (x_head, y_head + 1)

        if self.direction == "left":
            x_head, y_head = self.get_head_coordinates()
            self.body[0] = (x_head - 1, y_head)

        if self.direction == "right":
            x_head, y_head = self.get_head_coordinates()
            self.body[0] = (x_head, y_head + 1)

        # Snake is out of bounds
        if -1 in self.get_head_coordinates() or 400 in self.get_head_coordinates():
            self.lost = True
