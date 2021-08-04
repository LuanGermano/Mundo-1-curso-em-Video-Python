#Crie um programa que leia um numero inteiro e mostre na tela se ele é par o impar

#USA RESTO LUAN DIVIDINDO POR 2

num = int(input('Digite um numero inteiro qualquer: '))
n1 = num % 2
if n1 == 0:
    print ('Seu valor é par')
else:
    print ('seu valor é impar')