import unittest

from creamatrix import leggivda


class TestCreamatrix(unittest.TestCase):

    def test_read_vda(self):
        actual = leggivda(open("valid.vda", "r"), 3)

        self.assertIs(len(actual), 28, "actual holes should be 28")
