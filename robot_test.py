import unittest

from  robot import Robot

class RobotTest(unittest.TestCase):

#al crear este setup puedo utilizar self.megaman para ahorrarme escribir siempre el nombre y el nivel de bateria en cada test
    def setUp(self):
        self.megaman = Robot('Mega man', bateria=50)
        print("setUp siendo ejecutado")

    def test_cargar(self):
        self.megaman .cargar()
        self.assertEqual(self.megaman .bateria, 100)

    def test_decir_nombre(self):
        self.assertEqual(self.megaman .decir_nombre(), 'Me llamo Mega man')
        self.assertEqual(self.megaman .bateria, 49, 'La bateria deberia ser 49%')

    def tearDown(self):
        print("TearDown siendo ejecutado")

if __name__ == '__main__':
    unittest.main()