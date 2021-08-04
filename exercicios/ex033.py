#Faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor
a = float(input('Digite o primeiro Numero: '))
b = float(input('Digite um segundo numero: '))
c = float(input('Digite o terceiro Numero: '))
if (a > b) and (a > c):
    print(f'O maior numero é {a:.1f} ')
elif (b > a) and (b > c):
    print(f'O maior Numero é {b:.1f} ')
else:
    print(f'O maior Numero é {c:.1f} ')

if (a < b) and (a < c):
    print(f'O menor Numero é {a:.1f} ')
elif (b < a) and (b < c):
    print(f'O menor numero é {b:.1f} ')
else:
    print(f'O menor numero é {c:.1f}')
