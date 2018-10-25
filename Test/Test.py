import unittest
from io import IOBase

from aprifiles import aprivda, ReturnFile


class TestAll(unittest.TestCase):
    def setUp(self):
        self.filename = 'C:/Users/Amon/Documents/coding/HTG/filetestarea/test.vda'
        self.fail_file = 'H:/Pippo/culo.vda'
        self.no_file = None

    def test_apri(self):
        actual_obj = aprivda(self.filename)
        try:
            actual_obj.in_file.close()
        except AttributeError:
            pass
        else:
            pass
        expected_f = 'test.'
        actual_f = actual_obj.f
        expected_p = 'C:/Users/Amon/Documents/coding/HTG/filetestarea'
        actual_p = actual_obj.p
        self.assertEqual(expected_f, actual_f, 'FILE NON TROVATO')
        self.assertEqual(expected_p, actual_p, "CARTELLA NON GENERATA")
        self.assertIsInstance(actual_obj.in_file, IOBase, "IL FILE NON È VISTO COME TALE")
        actual_obj = aprivda(self.fail_file)
        expected_f = 0
        actual_f = actual_obj.f
        expected_p = 0
        actual_p = actual_obj.p
        self.assertEqual(expected_f, actual_f, 'IN CASO DI FILE ERRATO IL FALLBACK NON FUNZIONA')
        self.assertEqual(expected_p, actual_p, 'IN CASO DI FILE ERRATO IL FALLBACK NON FUNZIONA')
        actual_obj = aprivda(self.no_file)
        expected_f = 0
        actual_f = actual_obj.f
        expected_p = 0
        actual_p = actual_obj.p
        self.assertEqual(expected_f, actual_f, 'IN CASO DI FILE ASSENTE IL FALLBACK NON FUNZIONA')
        self.assertEqual(expected_p, actual_p, 'IN CASO DI FILE ASSENTE IL FALLBACK NON FUNZIONA')


if __name__ == '__main__':
        unittest.main()