#Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
#Ex.1:
import random
p1 = str(input('Primeiro aluno: '))
p2 = str(input('Ssegundo aluno: '))
p3 = str(input('Terceiro aluno: '))
p4 = str(input('Quarto aluno: '))
list = [p1, p2, p3, p4]
sorteio = random.choice(list)
print('O aluno sorteado para apagar o quadro foi {}'.format(sorteio))
#Ex.2:
from random import choise
p1 = str(input('Primeiro aluno: '))
p2 = str(input('Ssegundo aluno: '))
p3 = str(input('Terceiro aluno: '))
p4 = str(input('Quarto aluno: '))
list = [p1, p2, p3, p4]
sorteio = choise(list)
print('O aluno sorteado foi {}'.format(sorteio))