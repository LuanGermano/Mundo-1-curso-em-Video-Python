#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
#mostre quantos dólares ela pode comprar
#US$ 1,00 = R$3,27
n = float(input('Quantos Reais voce possui? '))
d = 3.27
c = n / d
print(f'Seus {n} Reais equivalem a US${c:.2f}')

