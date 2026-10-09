#Escreva um programa que converta uma temperatura digitando em °C e converta para °F
c = float(input('Informe a temperatura em °C: '))
f = ((9 * c) / 5) + 32
print('A temperatura de {}°C correspomde a {}°F!'.format(c, f))