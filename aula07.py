#Operações Aritiméticas
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro número: '))
s = n1+ n2
print('A soma vale {}'.format(s))

n1 = int(input('Um valor: '))
n2 = int(input('Outro número: '))
print('A soma vale {}'.format(n1+n2))

n1 = int(input('Um valor: '))
n2 = int(input('Outro número: '))
s = n1+ n2
m = n1* n2
d = n1/n2
di = n1//n2
e = n1**n2
rd = n1%n2
print('A soma é {}, \n o produto é {}, \n a divisão é {:.3f}'.format(s, m, d), end='. ')
print('\n A divisão inteira é {}, \n a exponeciação é {}, \n o resto da divisão é {}'.format(di, e, rd))