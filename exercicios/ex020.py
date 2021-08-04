#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
#faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
a1 = str(input('Qual o nome do primeiro aluno: '))
a2 = str(input('Qual o nome do segundo aluno: '))
a3 = str(input('Qual o nome do terceiro aluno: '))
a4 = str(input('Qual o nome do Quarto aluno: '))
lista =[a1, a2, a3, a4]

r = random.sample(lista, k=4)

print(f' a ordem sorteada dos alunos sera: \n{r} ')

