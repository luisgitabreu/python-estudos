#Desenvolva um programa que leia as 2 notas de um aluno, calcule e mostre sua média.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
s = (n1+ n2)/2
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, s))