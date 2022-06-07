'''
soma +
subtração - 
multiplicação *
divisão /
divisão inteira //
divisão resto %
exponenciação **
igual ==

####

Ordem de precedência 
1 ( )
2 **
3 * / // % 
(se estiver mais de um na mesma expressão, executar qual estiver primeiro, na ordem que aparece)
4 + -

####

calcular raiz quadrada == elevar a meio
raíz quadrada de 81 é 9
8**(1/2)

'''

# podemos usar operadores com string
print('um' + 'dois')
print('='*20)

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
soma = n1 + n2
mult = n1 * n2
div = n1 / n2
print(f'A soma é {soma}, a multiplicação é {mult} e a divisão é {div}.')
# mesma coisa que o de cima, porém com quebra de linha
print(f'A soma é {soma},\n a multiplicação é {mult}\n e a divisão é {div}.')
print(f'A soma vale {n1+n2}.')
# para não quebrar linhas, mesmo com diferentes prints, usar end='' no final. Porém se algo for adicionado às aspas, o valor será apresentado entre os diferentes print
print(f'Soma: {soma}.', end=' ')
print(f'Multiplicação: {mult}.', end=' ')
print(f'Divisão: {div}.')