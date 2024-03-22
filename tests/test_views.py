import unittest
from interface_grafica.views import calcular_mdc

class TestCalcularMDC(unittest.TestCase):
    def test_calculo_mdc(self):
        resultado = calcular_mdc(24, 36)
        self.assertEqual(resultado, 12)

    def test_calculo_mdc_igualdade(self):
        resultado = calcular_mdc(10, 10)
        self.assertEqual(resultado, 10)

    def test_calculo_mdc_primos(self):
        resultado = calcular_mdc(7, 11)
        self.assertEqual(resultado, 1)
