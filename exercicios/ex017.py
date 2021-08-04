#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo
#Calcule e mostre o comprimento da hipotenusa
from math import pow, sqrt, hypot

catop = float(input('Digite o Valor do cateto oposto: '))
catad = float(input('Qual o valor do Adjacente? '))
hipo =sqrt(pow(catop,2) + pow(catad,2))
hypot(catop, catad)
print(f'A hipotenusa do triangulo será {hipo} ')
