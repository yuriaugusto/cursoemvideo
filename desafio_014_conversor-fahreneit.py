print('Desafio 014:\nEscreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.')

tempC = float(input('Digite a temperatura em Cº: '))

tempF = (1.8 * tempC) + 32

print(f'{tempC}Cº é equivalente à {tempF:.1f}Fº.')