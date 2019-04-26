import re


class MapSizeError(Exception):
    pass


class InvalidInstructions(Exception):
    pass


class InstructionParser:
    START_COOR_REGEX = re.compile(r'^\d\d[NSEW]$')
    INSTRUCTION_REGEX = re.compile(r'^[FRL]+$')

    def is_valid_start_position(self, line):
        return self.START_COOR_REGEX.match(line)

    def is_valid_instructions(self, line):
        return self.INSTRUCTION_REGEX.match(line)

    def start_position(self, line):
        x, y = [int(x) for x in line[0:2]]
        return (x, y, line[2])

    def instructions(self, line):
        if self.is_valid_instructions(line):
            instructions = self.remove_whitespace(line)
        else:
            raise InvalidInstructions('Invalid instructions supplied {line}')

        return instructions

    def remove_whitespace(self, line):
        return line.strip().replace(' ', '')

    def bounds(self, line):
        x, y = [int(x) for x in line.split(' ')]

        if x <= 0 or y <= 0:
            raise MapSizeError(
                'Upper right coordinate invalid, needs to be a postive integer but received x: {x} and y: {y}')

        return (x, y)
