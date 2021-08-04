#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
from random import choice

a1 = str(input('Qual o nome do primeiro aluno: '))
a2 = str(input('Qual o nome do segundo aluno: '))
a3 = str(input('Qual o nome do terceiro aluno: '))
a4 = str(input('Qual o nome do Quarto aluno: '))
lista =[a1, a2, a3, a4]

esc = choice(lista)

print(f'o aluno escolhido foi o {esc}! ')
