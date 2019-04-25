class InvalidInstruction(Exception):
    pass


class Robot:
    ORIENTATION_MASKS = {
        'N': (0, 1),
        'S': (0, -1),
        'W': (-1, -0),
        'E': (1, 0)
    }

    ORIENTATION_ORDER = 'NESW'

    def __init__(self, position, bounds):
        self.position = position
        self.bounds = bounds
        self.commands = {
            'F': self.forward,
            'L': self.turn_left,
            'R': self.turn_right
        }

    def run(self, instructions):
        for instruction in instructions:
            if self.commands[instruction]:
                self.position = self.commands[instruction]()
            else:
                raise Exception

        return self.position

    def forward(self):
        x, y, orientation = self.position
        mask = self.ORIENTATION_MASKS[orientation]
        return tuple(a + b for a, b in zip((x, y), mask)) + (orientation,)

    def turn(self, direction):
        x, y, orientation = self.position
        orientation_index = self.ORIENTATION_ORDER.find(orientation)
        index = direction(orientation_index)
        return (x, y, self.ORIENTATION_ORDER[index])

    def turn_left(self):
        return self.turn(lambda index: index - 1)

    def turn_right(self):
        return self.turn(lambda index: 0 if index + 1 >= len(self.ORIENTATION_ORDER) else index + 1)
