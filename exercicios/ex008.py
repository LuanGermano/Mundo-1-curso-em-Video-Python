#escreva um programa que leia um valor em metros e o exiba convertido em centimetro e milimetros

m = float(input('Digite um valor de metro: '))
dm = m *10
cm = m * 100
mm = m * 1000
dam = m / 10
hm = m / 100
km = m / 1000

print(f'o seu valor de {m:.2f}m convertidos em centrimetros dara {cm}cm e para milimetro são {mm}mm ')
print(f' Decimetro é {dm}dm\n o decametro é {dam}Dm\n hectametro {hm}Hm\n e o kilometro {km}Km  ')