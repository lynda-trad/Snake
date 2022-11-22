class Snake:
    def __init__(self):
        self.x_init = 199
        self.y_init = 199
        self.body = [(self.x_init, self.y_init)]
        self.direction = "down"

    def get_head_coordinates(self):
        return self.body[0]

    def update_direction(self):
        self.direction = ""
