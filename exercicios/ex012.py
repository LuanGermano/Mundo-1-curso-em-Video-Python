#Faça um Algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Qual o valor do seu produto? '))
desc = 0.05
precod = preco * (1-desc)

print(f'Olá, seu produto de R${preco:.2f} estará saindo por R${precod:.2f}' )