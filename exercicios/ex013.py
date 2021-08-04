#faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento.
sal = float(input('Seu salario atual? '))
reaj = 0.15
nsal = sal * (1 + reaj)

print(f'Seu salario aumentou de R${sal:.2f} para R${nsal:.2f}, parabens por seu aumento! ')
