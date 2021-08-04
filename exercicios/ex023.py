#Faça um programa que leia de 0 a 9999 e mostre na tela cada um dos digitos separados.
# ex: digite um numero: 1834
#unidade: 4 dezena: 3 centena:8 Milhar: 1
num = int(input('Digite um Numero: '))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10
print(f'Analise do numero {num} ')
print(f'Unidade dele é {uni}')
print(f'Dezena dele é {dez} ')
print(f'Centena dele é {cen} ')
print(f'milhar dele é {mil} ')

