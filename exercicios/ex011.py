#Faça um programa que leia a largura e a altura de uma parede em metros,
#Calcule a sua area e a quantidade de tinta necessaria para Pinta-la,
#Sabendo que cada litro de tinta pinta uma area de 2m²

larg =float(input('Qual a largura da parede em metros? '))
altu =float(input('Qual a altura em metros? '))
ar= larg * altu
litro = 2
tintas= ar / litro

print(f'Sua parede tem {ar:.3f}m² e para ela serão necessarios {tintas:.2f} Litros de Tinta para ser pintada')