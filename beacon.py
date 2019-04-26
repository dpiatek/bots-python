class Beacon:
    def __init__(self, bounds):
        self.bounds = bounds
        self.position = None
        self.lost = False

    def ping(self, position):
        out_of_bounds = self.out_of_bounds(position)

        if out_of_bounds:
            self.lost = True
        else:
            self.position = position

        return not out_of_bounds

    def out_of_bounds(self, position):
        x, y, _ = position
        max_x, max_y = self.bounds
        return x > max_x or y > max_y or x < 0 or y < 0

    def result(self):
        return ' '.join([str(x) for x in self.position]) + (' LOST' if self.lost else '')
