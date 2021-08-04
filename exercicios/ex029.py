#Escreva um programa que leia a velocidade de um carro
#Se ele ultrapassar  80km/h, mostre uma mensagem falando que foi multado.
#A Multa vai custar R$7 por cada Km acima do limite

velc = float(input('Qual a velocidade o carro estava em Km/h? '))
if velc >= 81.0:
    exce = (velc - 80) * 7
    print(f'Vc foi multado no valor de R${exce:.2f} por excesso de velocidade ')
else:
    print('Esta tudo Ok')
