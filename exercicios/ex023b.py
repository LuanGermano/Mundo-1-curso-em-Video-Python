num = int(input( "Digite um valor de 0 a 9999: "))
num1 = str(num)
num2 = num1.zfill(4)
print('Unidade: {}'.format(num2[3]))
print('Dezena: {}'.format(num2[2]))
print('Centena: {}'.format(num2[1]))
print('Milhar: {}'.format(num2[0]))
