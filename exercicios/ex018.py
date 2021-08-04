#faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo

from math import cos,sin,tan, cos, radians

ang = float(input('Qual o valor do angulo? '))
rang = radians(ang)
print(f'O seu angulo de {rang}º tem os seguintes valores: \nCosseno: {cos(rang):.3f} \nSeno: {sin(rang):.3f} \nTangente: {tan(rang):.3f} ')
