import unittest
from main import soma

class TestSoma(unittest.TestCase):
    def test_soma_positiva(self):
        self.assertEqual(soma(1, 2), 3)

    def test_soma_negativa(self):
        self.assertEqual(soma(-1, -1), -2)

    def test_soma_zero(self):
        self.assertEqual(soma(0, 0), 0)
