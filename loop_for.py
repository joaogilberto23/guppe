"""
Loop -> Estrutura de repetição
For -> Uma destas estruturas

C# ou Java:

for(int i=0; i<n; i++){
    //execução do loop
}

Python:

for item in iterável:
    //execução do loop

Loops são utilizados para iterar sobre sequência ou valores iteráveis

Exemplos:

- String
    nome = 'João Gilberto'
- Lista
    lista = [1, 2, 3, 4, 5]
- Range
    range(1, 10)
"""
from builtins import print, range

nome = 'João Gilberto'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Tem que transformar em uma lista

# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando em uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando em um range)
for numero in range(1, 10):
    print(numero)
"""
OBS range: No range, o valor final é apenas uma referência, ele não é incluído na "impressão".
"""
qtd = int(input('Quantas vezes esse loop deve rodar?'))
for n in range(1, qtd + 1):
    print(f'Imprimindo {n}')

#############################################

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd + 1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

#############################################
