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


