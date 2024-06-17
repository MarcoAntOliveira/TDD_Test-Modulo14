"""
TDD - Test Driven Development

Red
Parte 1 - criar o teste e ver falhar

Green
Parte2 - criar o codigo e ver oteste passar

refactor
Parte3 - melhorar meu codigo 

"""
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
from baconcomovos import bacon_com_ovos

class TesteBaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos_deve_levantar_assertion_error_se_nao_receber_int(self):
        with self.assertRaises(AssertionError):
           bacon_com_ovos(' ')

    def test_bacon_com_ovos_deve_retornar_bacon_com_ovos_se_entrada_for_multiplo_de_3_e_5(self):
      entradas = (15, 30, 45, 60)
      saida = "Bacon com ovos"
      for entrada in  entradas:
         self.assertEqual(
            bacon_com_ovos(entrada), 
            saida,
            msg=f"{entrada} nao retornou {saida}"
            )
         
    def test_bacon_com_ovos_deve_retornar_passar_fome_se_entrada_nao_for_multiplo_de_3_e_5(self):
      entradas = (1,2,4, 7, 8)
      saida = "Passa fome"
      for entrada in  entradas:
         self.assertEqual(
            bacon_com_ovos(entrada), 
            saida,
            msg=f"{entrada} nao retornou {saida}"
            )     

         
    def test_bacon_com_ovos_deve_retornar_bacon_se_entrada_nao_for_multiplo_de_3(self):
      entradas = (3, 6, 9, 12, 18)
      saida = "Bacon"
      for entrada in  entradas:
         self.assertEqual(
            bacon_com_ovos(entrada), 
            saida,
            msg=f"{entrada} nao retornou {saida}"
            )  

    def test_bacon_com_ovos_deve_retornar_ovos_se_entrada_nao_for_multiplo_de_5(self):
      entradas = (5, 10, 20, 25)
      saida = "Ovos"
      for entrada in  entradas:
         self.assertEqual(
            bacon_com_ovos(entrada), 
            saida,
            msg=f"{entrada} nao retornou {saida}"
            )     
        

         


if __name__ =="__main__":
   unittest.main(verbosity = 2)            