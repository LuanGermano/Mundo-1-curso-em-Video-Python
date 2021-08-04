#crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

name = str(input('Digite o nome de uma cidade: ')).title().split()
print(f'A existencia da palavra Santo no inicio da cidade é {"Santo" in name[0]} ')



