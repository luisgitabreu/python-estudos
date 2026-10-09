#Escreva um programa que leia um valor em metros e o exiba em centímetros e milímetros.
medida = float(input('Distância em metros: '))
cm = medida* 100
mm = medida* 1000
print('Dada a medida em {}m, convertido em centímetros é {}cm e em milímetros é {}mm.'.format(medida, cm, mm))

#Programa melhorado
med = float(input('Distância em metros: '))
km = med/1000
hm = med/100
dam = med/10
dm = med*10
cm = med* 100
mm = med* 1000
print('A distância de {}m convertida, é:\n{}km\n{}hm\n{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(med, km, hm, dam, dm, cm, mm))