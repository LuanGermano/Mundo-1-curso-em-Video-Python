#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$ 0,15 por Km rodado.
cdia = 60
ckm = 0.15
km = float(input('Quantos Kilometros foram rodados? '))
dia =int(input('Quantos dias se passaram com o Carro? '))
c1 =km * ckm
c2 =dia * cdia
custo = c1 + c2

print(f'De acordo com os {dia} dias decorridos os {km:.0f} rodados sua conta será no valor de R${custo:.2f} ')
