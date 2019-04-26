import re

from instruction_parser import InstructionParser
from robot import Robot
from tracker import Tracker


class Main:
    def run(self, parser, path):
        f = open(path)
        bounds = parser.bounds(f.readline())
        tracker = Tracker(bounds)

        for raw_line in f:
            line = parser.remove_whitespace(raw_line)

            if parser.is_valid_start_position(line):
                start_position = parser.start_position(line)
                instructions = parser.instructions(f.readline())
                robot = Robot(position=start_position, ping=tracker.beacon(),
                              scents=tracker.scents())
                robot.run(instructions)

        f.close()

        return tracker.results()


if __name__ == "__main__":
    import sys
    main = Main()
    parser = InstructionParser()
    output = main.run(parser, sys.argv[1])
    print(output)
