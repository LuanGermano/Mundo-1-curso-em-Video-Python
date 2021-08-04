#Desenvolva um programa que pergunte a distancia de uma viagem em KM.
#Calcule o preço da passagem, cobrando R$0,50 por km para viagens de ate 200 Km
# e R$0,45 para viagens mais longas.

dist = float(input('Qual a distancia em Kilometros até o seu destino? '))
if dist <= 200.00:
    d1 = dist * 0.50
    print(f'O valor da sua passagem será de R${d1:.2f} ')
else:
    d1 = dist * 0.45
    print(f'O valor da sua passagem será de R${d1:.2f} ')
