import unittest

from KG_dxf import Forotag
from infrastructure import DrawingExchangeFormatConfigurations


class TestKgDxf(unittest.TestCase):

    def test_foroTagStrangeConversion(self):
        i = 1
        cf = DrawingExchangeFormatConfigurations("./")

        cx = 2
        cy = 3
        cz = 4
        cr = 5
        exec('foro%d = Forotag(%d,%d,%d,%d,%s,%f,%d,4,"%s","%s","%s","%s","%s","%s")' % (i,cx,cy,cz,cr,
                                                                                   cf.htesto,cf.angolo,i,
                                                                                   cf.cer_colore,cf.cer_livello,
                                                                                   cf.etk_colore,cf.etk_livello,
                                                                                   cf.tes_livello,cf.tes_colore))
        self.assertIsNotNone(Forotag(cx,cy,cz,cr,
                                     cf.htesto,cf.angolo,i, 4,
                                     cf.cer_colore,cf.cer_livello,
                                     cf.etk_colore,cf.etk_livello,
                                     cf.tes_livello,cf.tes_colore))

    def test(selfself):
        print(5 if 1 else 7)


if __name__ == '__main__':
    unittest.main()
