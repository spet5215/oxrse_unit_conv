import unittest
from oxrse_unit_conv.units import g, kg


class TestGram(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(g.si_unit.matches(kg))

    def test_basic_conversion(self):
        self.assertEqual(g.to_si(1), 0.001)
        self.assertAlmostEqual(g.to_unit(10, g), 10, 8)


if __name__ == '__main__':
    unittest.main()
