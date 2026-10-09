#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira. Ex.: Digite um número: 6.127 O número 6.127 tem a parte inteira 6.
#Ex.1:
import math
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.floor(num)))

#Ex.2:
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))

#Ex.3:
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))