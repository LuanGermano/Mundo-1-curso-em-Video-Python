#Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.
t1 = float(input('Qual a temperatura atual em celsius? '))
t2 = t1 * (9 / 5) + 32

print(f'A temperatua de {t1:.1f}ºC que vc esta sentindo corresponde a {t2:.1f}ºF \nmas sabia que lá em curitiba é de {t1-9}ºC???')

