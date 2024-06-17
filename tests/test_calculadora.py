try:
    import sys
    import os
    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except:
    raise
import unittest
from calculadora import soma

class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5, 5), 10)
        
    def test_soma_5_negativo_e_5_deve_retornar_0(self):
        self.assertEqual(soma(-5, 5), 0)

    def teste_soma_varias_entradas(self):
        x_y_saidas =(
            (10, 10, 20),
            (5, 5, 10),
            (1.5, 1.5, 3.0),
            (10, 10, 20),
            (10, 20, 30),

        )    
        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida = x_y_saida):
                    x, y, saida = x_y_saida
                    self.assertEqual(soma(x, y), saida) 

    def soma_x_nao_int_ou_float_retorna_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma(2, "a")  
       
    def soma_y_nao_int_ou_float_retorna_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma("a", 2)  
          

if __name__ == "__main__":       
    unittest.main(verbosity= 2)