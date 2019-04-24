import re


class MapSizeError(Exception):
    pass


class InstructionError(Exception):
    pass


class InstructionParser:
    INSTRUCTION_REGEX = re.compile(r'^[FRL]+$')
    START_COOR_REGEX = re.compile(r'^\d\d[NSEW]$')

    def parse_start_coor(self, line):
        x, y = [int(x) for x in line[0:2]]
        orientation = line[2]
        return {'init': {'x': x, 'y': y, 'orientation': orientation}}

    def parse_instructions(self, line):
        return {'instructions': line}

    def remove_whitespace(self, line):
        return line.strip().replace(' ', '')

    def parse_line(self, raw_line):
        line = self.remove_whitespace(raw_line)

        if self.START_COOR_REGEX.match(line):
            data = self.parse_start_coor(line)
        elif self.INSTRUCTION_REGEX.match(line):
            data = self.parse_instructions(line)
        else:
            raise InstructionError(
                'Invalid coordinate or instruction given: {line}')
        return data

    def parse_size(self, line):
        x, y = [int(x) for x in line.split(' ')]

        if x <= 0 or y <= 0:
            raise MapSizeError(
                'Upper right cooridinate invalid, needs to be a postive integer but received x: {x} and y: {y}')

        return {'x': x, 'y': y}

    def merge_data(self, data):
        return {**data[0], **data[1]}

    def parse(self, path):
        with open(path) as f:
            size = self.parse_size(f.readline())
            parsed_lines = [self.parse_line(line)
                            for line in f if line != '\n']
            robots = [self.merge_data(
                parsed_lines[x:x+2]) for x in range(0, len(parsed_lines) - 1, 2)]
        f.closed

        return {**size, 'robots': robots}
