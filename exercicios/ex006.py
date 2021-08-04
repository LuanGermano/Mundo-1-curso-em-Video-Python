#Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e Raiz quadrada
from cor import cores
n = int(input('Digite um numero: '))
n1 = n * 2
n2 = n * 3
n3 = n ** (1/2)

print(f'{cores["cya"]}o seu numero é {n} \no dobro dele é {n1}, \no triplo {n2} \ne a raiz quadrada é {n3:.2f}.')
