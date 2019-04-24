import unittest
from instruction_parser import InstructionParser, MapSizeError, InstructionError


class InstructionParserTest(unittest.TestCase):
    parser = InstructionParser()

    def test_parse_instructions(self):
        self.assertEqual(self.parser.parse_instructions('RFRFRFRF'), {
            'instructions': 'RFRFRFRF',
        })

    def test_parse_start_coor(self):
        self.assertEqual(self.parser.parse_start_coor('11E'), {
            'init': {
                'x': 1, 'y': 1, 'orientation': 'E'
            },
        })

    def test_parse_size(self):
        self.assertEqual(self.parser.parse_size('5 3'), {'x': 5, 'y': 3})

    def test_parse_size_error(self):
        with self.assertRaises(MapSizeError):
            self.parser.parse_size('-5 3')

    def test_parse_line(self):
        with self.assertRaises(InstructionError):
            self.parser.parse_line('')
        self.assertEqual(self.parser.parse_line('1 1 E'), {
            'init': {
                'x': 1, 'y': 1, 'orientation': 'E'
            },
        })
        self.assertEqual(self.parser.parse_line('RFRFRFRF'), {
            'instructions': 'RFRFRFRF',
        })

    def test_parse(self):
        path = 'sample_input.txt'
        output = {
            'x': 5,
            'y': 3,
            'robots': [
                {
                    'init': {
                        'x': 1, 'y': 1, 'orientation': 'E'
                    },
                    'instructions': 'RFRFRFRF'
                },
                {
                    'init': {
                        'x': 3, 'y': 2, 'orientation': 'N'
                    },
                    'instructions': 'FRRFLLFFRRFLL'
                },
                {
                    'init': {
                        'x': 0, 'y': 3, 'orientation': 'W'
                    },
                    'instructions': 'LLFFFLFLFL'
                },
            ]}
        self.assertEqual(self.parser.parse(path), output)


if __name__ == '__main__':
    unittest.main()
