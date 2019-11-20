"""
Faça um programa que recebna dois números e mostre qual deles é o maior
"""
num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')

if num1 > num2:
    print(f'O número maior é o: {num1}')
elif num1 == num2:
    print('Os números são iguais!')
else:
    print(f'O número maior é o: {num2}')
