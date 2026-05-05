import unittest
import requests 

from app import calcular_desconto

class TestCalculadoraDesconto(unittest.TestCase):
    def test_calculo_desconto_100(self):
        self.assertAlmostEqual(calcular_desconto(100), 90.0)

    def test_calculo_desconto_200(self):
        self.assertAlmostEqual(calcular_desconto(200), 180.0)

    def test_preco_none(self):
        self.assertIsNone(calcular_desconto(None))

if __name__ == "__main__":
    unittest.main()