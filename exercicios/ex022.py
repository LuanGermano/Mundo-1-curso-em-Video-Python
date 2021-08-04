# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas minusculas e maiusculas
# Quantas letras ao todo(sem considerar espaços)
# Quantas letras tem o primeiro nome?

name = str(input('Qual o seu nome completo? ')).strip()
nsplit = name.split()
print((f'O seu nome com todas as letras minusculas  é {name.lower()},'
       f'\ne todas as letras maiusculas seria {name.upper()} '
       f'\nTem {len("".join(nsplit))} letras, \n'
       f'e no seu primeiro nome que é {nsplit[0]} tem {len(nsplit[0])} letras! '))
