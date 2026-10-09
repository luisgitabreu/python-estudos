#Código 01
n1 = input('Digite um valor: ')
print(type(n1))

#Código 02
n1 = int(input('Digite um valor: '))
print(type(n1))

#Código 03
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
print('A soma ente {} e {}, vale {}'.format(n1, n2, s))

#Tipos de Formato
n = float(input('Digite um valor: '))
print(n)
n = bool(input('Digite um valor; '))
print(n)
n = input('Digite um valor: ')
print(n.isnumeric())