"""
10. Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
utilizando as seguintes fórmulas (onde h corresponde à altura):
* Homens: (72.7 * h) - 58
* Mulheres: (62.1 * h) - 44.7
"""
import sys

altura = float(input(f'Qual a sua altura? (Ex: 1.72): '))
sexo = input(f'Qual o seu sexo? (M ou F): ')

if sexo not in ['M', 'm', 'F', 'f']:
    print(f'Informação de sexo inválida!')
    sys.exit()

if sexo in ['M', 'm']:
    pesoIdeal = (72.7 * altura) - 58
    print(f'Seu peso ideal é: {pesoIdeal}Kg')
else:
    pesoIdeal = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é: {pesoIdeal}Kg')
