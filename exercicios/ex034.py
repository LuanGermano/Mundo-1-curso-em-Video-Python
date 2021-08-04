#Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
#para salarios superiores a 1250 calcule aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%

sal = float(input('Qual o seu salario atual? R$'))
aum1 = 1.10
aum2 = 1.15
if sal <= 1250.00:
    a1 = sal * aum2
    print(f'O seu novo salario sera de R${a1:.2f} ')
else:
    a2 = sal * aum1
    print(f'O seu novo Salario sera de R${a2:.2f} ')
