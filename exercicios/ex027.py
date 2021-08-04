#Faça um programa que leia o nome completo de uma pessoa,
# Mostrando em seguida o primeiro e o Ultimo nome separadamente.
#Ex: Ana maeria de Souza
#Primeiro = Ana Ultimo = Souza

name = str(input('Digite seu nome completo: ')).title().split()
namep = name[0]
namel = name[len(name)-1]
print(f'Seu primeiro Nome é {namep} e o ultimo nome é {namel}')