import unittest

from KG_dxf import Forotag, Cerchio
from infrastructure import DrawingExchangeFormatConfigurations


class TestKgDxf(unittest.TestCase):

    def test_initialize_circle(self):
        actual = Cerchio(10, 20, 30, 40, 'Bori', 50)

        expected = """0
CIRCLE
8
Bori
10
10
20
20
30
30
40
40
62
50
"""
        self.assertEqual(actual.dxfcode, expected)

    def test_initialize_circle_no_colour(self):
        actual = Cerchio(10, 20, 30, 40, 'Bori')

        expected = """0
CIRCLE
8
Bori
10
10
20
20
30
30
40
40
62
0
"""
        self.assertEqual(actual.dxfcode, expected)


if __name__ == '__main__':
    unittest.main()
