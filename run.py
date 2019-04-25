import re

from instruction_parser import InstructionParser
from robot import Robot


class Main:
    START_COOR_REGEX = re.compile(r'^\d\d[NSEW]$')

    def __init__(self):
        self.parser = InstructionParser()

    def run(self, path):
        f = open(path)
        bounds = self.parser.bounds(f.readline())
        results = []

        for raw_line in f:
            line = self.parser.remove_whitespace(raw_line)

            if self.START_COOR_REGEX.match(line):
                start_coord = self.parser.start_coord(line)
                instructions = self.parser.remove_whitespace(f.readline())

                robot = Robot(start_coord, bounds)
                result = robot.run(instructions)

                results.append(result)

        f.close()

        return results


if __name__ == "__main__":
    import sys
    main = Main()
    output = main.run(sys.argv[1])
    print(output)
