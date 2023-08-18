import unittest

from testes_codigo import comer, dormir


class TestesCodigoTest(unittest.TestCase):
    def test_comer_saludable(self):
        self.assertEqual(
            comer('arroz', True),
            'Estoy comiendo arroz porque Quiero estar en forma'
        )

    def test_comer_rico(self):
        self.assertEqual(
            comer(comida='pizza', saludable=False),
            'Estoy comiendo pizza porque Hoy me apetece comer porqueria'
        )

    def test_dormir_poco(self):
        self.assertEqual(
            dormir(4),
            'Hay que dormir mas'
        )

    def test_dormir_mucho(self):
        self.assertEqual(
            dormir(14),
            'Hay que dormir menos, gandul!'
        )

if __name__ == '__main__':
    unittest.main()