class Robot:
    ORIENTATION_MASKS = {
        'N': (0, 1),
        'S': (0, -1),
        'W': (-1, -0),
        'E': (1, 0)
    }

    ORIENTATION_ORDER = 'NESW'

    def __init__(self, position, ping, scents):
        self.position = position
        self.scents = scents
        self.ping = ping

        self.commands = {
            'F': self.forward,
            'L': self.turn_left,
            'R': self.turn_right
        }

    def run(self, instructions):
        for instruction in instructions:
            self.position = self.commands[instruction]()

            if not self.ping(self.position):
                break

    def forward(self):
        x, y, orientation = self.position
        mask = self.ORIENTATION_MASKS[orientation]
        new_position = tuple(
            a + b for a, b in zip((x, y), mask)) + (orientation,)

        return self.position if self.position in self.scents else new_position

    def turn(self, direction):
        x, y, orientation = self.position
        orientation_index = self.ORIENTATION_ORDER.find(orientation)
        index = direction(orientation_index)
        return (x, y, self.ORIENTATION_ORDER[index])

    def turn_left(self):
        return self.turn(lambda index: index - 1)

    def turn_right(self):
        return self.turn(lambda index: 0 if index + 1 >= len(self.ORIENTATION_ORDER) else index + 1)
