#Desenolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou não formar um triangulo.
r1 = float(input('Digite o valor da Primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))

if (r2 + r3) > r1 > (r2 - r3) and (r1 + r3) > r2 > (r1 - r3) and (r1 + r2) > r3 > (r1 - r3):
     print('O triangulo é possivel!')
else:
    print('Deu ruim')
