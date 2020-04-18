"""
Loop -> Estrutura de repetição
For -> Uma destas estruturas

C# ou Java:

for(int i=0; i<n; i++){
    //execução do loop
}

Python:

for item in interavel:
    //execução do loop

Loops são utilizados para iterar sobre sequência ou valores iteráveis

Exemplos:

- String
    nome = 'João Gilberto'
- Lista
    lista = [1, 2, 3, 4, 5]
- Range
    range(1, 10)

OBS: No range, o valor final é apenas uma referência, ele não é incluído na "impressão".

Enumerate - Sequencia cada valor da variável em uma túpla especificanto seus índices.
Exemplo:
nome = 'João'

for variavel in enumerate(nome):
    print(variavel)

OBS: Quando não precisamos de um valor, descartamos o mesmo utilizando um underline ( _ ).

nome = 'João Gilberto'
for letra in nome:
    print(letra, end='')

OBS: a terminação END='' no print faz a impressão da variável ser horizontal.

"""



