import re


class MapSizeError(Exception):
    pass


class InstructionError(Exception):
    pass


class InstructionParser:
    INSTRUCTION_REGEX = re.compile(r'^[FRL]+$')
    START_COOR_REGEX = re.compile(r'^\d\d[NSEW]$')

    def start_coord(self, line):
        x, y = [int(x) for x in line[0:2]]
        return (x, y, line[2])

    def remove_whitespace(self, line):
        return line.strip().replace(' ', '')

    def bounds(self, line):
        x, y = [int(x) for x in line.split(' ')]

        if x <= 0 or y <= 0:
            raise MapSizeError(
                'Upper right coordinate invalid, needs to be a postive integer but received x: {x} and y: {y}')

        return (x, y)
