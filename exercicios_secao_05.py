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
import sys

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 == num2:
    print(f'Os números digitados são iguais!')
    sys.exit()
elif num1 > num2:
    print(f'O número maior é o: {num1}')
    numeroMaior = num1
    numeroMenor = num2
else:
    print(f'O número maior é o: {num2}')
    numeroMaior = num2
    numeroMenor = num1
print(f'A diferença entre os números é de: {numeroMaior - numeroMenor}')

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

"""
8. Faça um programa que leia duas notas de um aluno, verifique se as notas são válidas e exiba na tela a média
destas notas. Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua
valor válido, este fato deve ser informado ao usuário e o programa termina.
"""
import sys

num1 = float(input('Digite a primeira nota: '))
if num1 < 0.0 or num1 > 10.0:
    print(f'A primeira nota informada não é válida!')
    sys.exit()

num2 = float(input('Digite a primeira nota: '))
if num2 < 0.0 or num2 > 10.0:
    print(f'A segunda nota informada não é válida!')
    sys.exit()

print(f'A média do aluno é: {(num1 + num2) / 2}')

"""
9. Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que
20% do salário imprima: Empréstimo não concedido, caso contrário imprima: Empréstimo concedido.
"""
import sys

salario = float(input('Digite o valor do seu salário: '))
if salario <= 0:
    print(f'Valor de salário inválido!')
    sys.exit()

emprestimo = float(input('Digite o valor do empréstimo que deseja: '))
if emprestimo <= 0:
    print(f'Valor de empréstimo inválido!')
    sys.exit()

if emprestimo > (salario * 0.2):
    print(f'Empréstimo não concedido!')
else:
    print(f'Empréstimo concedido!')
    print(f'Saldo atualizado: {salario + emprestimo}')

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
    print(f'Seu peso ideal é: {pesoIdeal} Kg')
else:
    pesoIdeal = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é: {pesoIdeal} Kg')
