#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media
from cor import cores
n1 = float(input('Nota de portugues: '))
n2 = float(input('Nota de Matematica: '))
nm= (n1+n2)/2
if n1 >= 5:
    c1 = cores["Bblu"]
else:
    c1 = cores["Bred"]
if n2 >=5:
    c2 = cores["Bblu"]
else:
    c2 = cores["Bred"]
if nm >= 5:
    c3 = cores["Bblu"]
else:
    c3 = cores["Bred"]
print(f'A Nota de portugues do Aluno foi {c1}{n1:.1f}{cores["cle"]} e junto da nota de matematica que foi {c2}{n2:.1f}{cores["cle"]} \nO aluno obteve uma media final de {c3}{nm:.1f}{cores["cle"]} ')
