"""
1.Faça um programa que recebna dois números e mostre qual deles é o maior
"""
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print(f'O número maior é o: {num1}')
elif num1 == num2:
    print('Os números são iguais!')
else:
    print(f'O número maior é o: {num2}')

"""
2.Leia um número fornecido pelo usuário. Se esse número for positivo, caucule a raiz  quadrada
do número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
"""
num = float(input('Digite um número: '))

if num < 0:
    print('Número inválido!')
else:
    print(f'A raiz quadrada do número digitado é: {num ** 0.5}')

"""
3. Leia um número real. Se o número  for positivo imprima a raiz quadrada. Do Contrário,
imprima o número ao quadrado.
"""
num = float(input('Digite um número: '))

if num > 0:
    print(f'A raiz quadrada do número digitado é: {num ** 0.5}')
else:
    print(f'Este número ao quadrado é igual a: {num ** 2}')

"""
4. Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
* O número digitado ao quadradro; * A raiz quadrada do número digitado.
"""
num = float(input('Digite um número: '))

if num >= 0:
    print(f'Este número ao quadrado é igual a: {num ** 2}')
    print(f'A raiz quadrada deste número é igual a: {num ** 0.5}')
else:
    print(f'O número digitado não é válido!')

"""
5. Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar.
"""
num = int(input('Digite um número: '))

if num >= 0:
    if num % 2 == 0:
        print(f'Este número é igual par!')
    elif num % 2 != 0:
        print(f'Este número é igual ímpar!')
else:
    print(f'O número digitado não é válido!')

"""
6. Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles,
assim como a diferença existente entre ambos.
"""

"""
7. Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois números forem iguais,
imprima a mensagem 'Números iguais'.
"""
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 == num2:
    print('Os números são iguais!')
elif num1 > num2:
    print(f'O número maior é o: {num1}')
else:
    print(f'O número maior é o: {num2}')
