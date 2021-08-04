#Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e o seu antecessor
from cor import cores
n = int(input(f'{cores["red"]}fale um numero:{cores["cle"]} '))
print(f'{cores["blu"]}O seu numero é {n},{cores["cle"]} ')
print(f'{cores["gre"]}o Antecessor do seu numero é {n-1},{cores["cle"]} ')
print(f'{cores["yel"]}e o sucessor do seu numero é {n+1}.{cores["cle"]} ')



