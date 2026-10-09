#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. 
#Ex.1:
import math
ang = float(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O ângulo de {} tem o seno de {:.2f}\nO cosseno de {:.2f}\nA tangente de {:.2f}'.format(ang, sen, cos, tan))
#Ex.2:
#from math import sin, cos, tan, radians
ang = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ang))
print('O ângulo {} tem o seno de {:.2f}'.format(ang, seno))
cosseno = math.cos(math.radians(ang))
print('O ângulo {} tem o cosseno de {:.2f}'.format(ang, cosseno))
tangente = math.tan(math.radians(ang))
print('O ângulo de {} tem a tangente de {:.2f}'.format(ang, tangente))