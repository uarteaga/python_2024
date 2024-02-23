import unittest
import main

class test_main(unittest.TestCase):

    def setUp(self):
        print('Iniciando las pruebas automáticas del unittest para la función suma_cinco() ')

    def test_suma_cinco_uno(self):
        test_parameter = 5
        result = main.suma_cinco(test_parameter)
        self.assertEqual(result, 10)
        print('Validando 5 + 10 es correcto') 
        
    def test_suma_cinco_dos(self):
        test_parameter = 'string'
        result = main.suma_cinco(test_parameter)
        self.assertIsInstance(result, ValueError)
    
    def test_suma_cinco_tres(self):
        test_parameter = None
        result = main.suma_cinco(test_parameter)
        self.assertEqual(result, "Por favor ingresa un número: ")
    
    def test_suma_cinco_cuatro(self):
        test_parameter = ''
        result = main.suma_cinco(test_parameter)
        self.assertEqual(result, "Por favor ingresa un número: ")
    
if __name__ == '__main__':
    unittest.main()