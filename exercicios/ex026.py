#faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a Letra "A".
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a ultima vez.

frase = str(input('Digite uma frase qualquer: ')).lower().strip()
fr1 = frase.count('a')
fr2 = frase.find('a')+1
fr3 = frase.rfind('a')+1
print(f'Na sua frase aparecem {fr1}x a letra "a" sendo a sua primeira aparição na posição {fr2} e a ultima no {fr3} ')