from cor import cores
n1 = int(input('Primeiro número?'))
n2 = int(input('e o segundo?'))
res = n1 + n2

#print('resultado da soma entre {} e {} será igual a {}'.format(n1,n2,res))
print(f'a soma entre {cores["red"]}{n1}{cores["cle"]} e {cores["blu"]}{n2}{cores["cle"]} é igual a : {cores["Bpur"]}{n1+n2}{cores["cle"]}!')
