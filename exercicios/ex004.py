from cor import cores
n = input(f'{cores["cya"]}Digite algo:{cores["cle"]} ')
print(f'{cores["blu"]}o Tipo primitivo desse valor é da:', type(n))
print(f'Tem espaço?', n.isspace())
print(f'é um numero?', n.isnumeric())
print(f'é alfabetico?', n.isalpha())
print(f'é alfanumerico?', n.isalnum())
print(f'está em maiusculas?', n.isupper())
print(f'esta em minusculas?', n.islower())
print(f'esta capitalizada', n.istitle())
