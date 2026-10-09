#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
#Ex.1:
co = float(input('Comprimneto do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip = (co** 2 + ca** 2)**(1/2)
print('A hipotenusa do triângulo vai medir {:.2f}'.format(hip))
#Ex.2:
import math
co = float(input('Comprimneto do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa do triângulo vai medir {:.2f}'.format(hi))
#Ex.3:
from math import hypot
co = float(input('Comprimneto do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa do triângulo vai medir {:.2f}'.format(hi))