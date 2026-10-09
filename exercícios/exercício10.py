#Crie um programa que leia quanto de dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#Considere US$1,00 = R$3,27
#real = float(input('Quanto dinheiro você tem na carteira? R$'))
#dolar = real / 3.27
#print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.50
euro = real / 6.13
euro = dolar / 1.11
print('Com R${:.2f} você pode comprar US${:.2f} e €{:.2f}'.format(real, dolar, euro))
print('Com US${:.2f} você pode comprar €{:.2f}'.format(dolar, euro))