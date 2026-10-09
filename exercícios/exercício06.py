#Crie um algoritimo que leia um número e mostre o seu dobro, o seu triplo e raiz quadrada.
n1 = float(input('Digite um número: '))
n2 = 2
n3 = 3
s = n1 * n2
z = n1 * n3

print('O dobro de {} é {}!'.format(n1, s))
print('O seu triplo é {}!'.format(z))
print('E o seu valor em raiz quadrada é {:.2f}!'.format(pow(n1, (1/2))))

#Segundo código feito
n = float(input('Digite um número: '))
print('O dobro de {} é {}. \nO seu triplo é {}. \nSua raiz quadrada é {:.2f}'.format(n, (n*2), (n*3), (n**(1/2))))

#Resolução feita pelo professor
n = float(input('Digite um número: '))
d = n* 2
t = n* 3
r = n** (1/2)
print('O dobro de {} é {}. \n O triplo é {}. \n E a raiz quadrada é {:.2f}.'.format(n, d, t, r))
