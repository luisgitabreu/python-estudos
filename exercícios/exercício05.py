#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
n1 = int(input('Digite um número: '))
n2 = 1
s = n1+ n2
z = n1- n2
print('O seu sucessor é {}!'.format(s))
print('E o seu antecessor é {}!'.format(z))
#Resposta do professor
n = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))