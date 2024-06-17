"""
1. receber um numero inteiro  
2. saber se o numero e multiplo de 3 e 5
bacon com ovos
3. saver se o numero multiplio somente de 3
bacon
3. saver se o numero multiplio somente de 5
ovos
2. saber se onumero nao e multiplo de 3 e 5
passa fome

"""

def bacon_com_ovos(n):
   assert(isinstance(n, int))
   if(n % 5 == 0 and n % 3 ==0):
      return "Bacon com ovos"
   elif(n%3 == 0):
      return "Bacon"
   elif(n%5==0):
      return "Ovos"
   return "Passa fome"