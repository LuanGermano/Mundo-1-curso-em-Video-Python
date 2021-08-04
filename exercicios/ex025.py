#Crie um programa que leia o nome de uma pessoa e diga se ela tem "silva" no nome

name = str(input('Digite o seu nome completo? ')).strip().title()
n1 = name.split()
print(f'Seu nome completo é {name} e é {"Silva" in n1} que vc tem Silva no seu nome ')
