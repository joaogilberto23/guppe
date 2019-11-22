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

"""
Leia um número fornecido pelo usuário. Se esse número for positivo, caucule a raiz  quadrada
do número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
"""
num = input('Digite um número: ')

if float(num) < 0:
    print('Número inválido!')
else:
    print(f'A raiz quadrada do número digitado é: {float(num) ** 0.5}')

"""
Leia um número real. Se o número  for positivo imprima a raiz quadrada. Do Contrário,
imprima o número ao quadrado.
"""
num = input('Digite um número: ')

if float(num) > 0:
    print(f'A raiz quadrada do número digitado é: {float(num) ** 0.5}')
else:
    print(f'Este número ao quadrado é igual a: {float(num) ** 2}')

"""

"""