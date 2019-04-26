import unittest
from instruction_parser import InstructionParser, MapSizeError


class InstructionParserTest(unittest.TestCase):
    parser = InstructionParser()

    def test_start_position(self):
        self.assertEqual(self.parser.start_position('11E'), (1, 1, 'E'))

    def test_bounds(self):
        self.assertEqual(self.parser.bounds('5 3'), (5, 3))

    def test_remove_whitespace(self):
        self.assertEqual(self.parser.remove_whitespace('1 1 E'), '11E')


if __name__ == '__main__':
    unittest.main()
