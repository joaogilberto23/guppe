num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

while num1 > 0:
    if num1 == num2:
        print(f'Os números digitados são iguais!')
    break
    elif num1 > num2:
        numeroMaior = num1
        numeroMenor = num2
    else:
        numeroMaior = num2
        numeroMenor = num1
print(f'O maior é o: {numeroMaior}')
print(f'A diferença entre os números é de: {numeroMaior - numeroMenor}')

