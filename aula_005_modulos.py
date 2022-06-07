# Podemos importar módulos completos ou apenas uma parte do que precisamos dentro de um módulo.

'''
funções do módulo math (import math)
from math import sqrt, ceil - modo de importar apenas uma, ou mais, função do módulo 

ceil - arredonda pra cima
floor - arredonda pra baixo
trunc - truncar número, elimina da virgula pra frente
pow - potêcia
sqrt - raíz quadrada
factorial - calcular factorial
'''

import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print(f'A raíz quadrada de {num} é igual a {raiz}.')