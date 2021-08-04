#Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira
#ex: Digite um numero 6,127 "O numero 6,127 tem a parte inteira 6"
from math import trunc
num = float(input('Digite qualquer valor: '))

print(f'O valor de {num} tem como numero inteiro {trunc(num)} ')
