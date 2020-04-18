"""
Ranges são utilizados para  gerar sequências numéricas de forma não aleatória, especificada.

#Forma 1
range (valor_de_parada)
OBS: valor_de_parada, NÃO inclusive (início padrão 0 e passo de 1 em 1)
EX:
for num in range(11):
    print(num)

#Forma 2
range (valor_de_inicio, valor_de_parada)
OBS: valor_de_parada, NÃO inclusive (início padrão especificado pelo usuário e passo de 1 em 1)
EX:
for num in range(5, 11):
    print(num)

#Forma 3
range (valor_de_inicio, valor_de_parada, passo)
OBS: valor_de_parada, NÃO inclusive (início padrão especificado pelo usuário e passo especificado pelo usuário)
EX:
for num in range(2, 20, 2):
    print(num)

#Forma 4 (INVERSA)
range (valor_de_inicio, valor_de_parada, passo)
OBS: valor_de_parada, NÃO inclusive (início especificado pelo usuário e passo especificado pelo usuário)
EX:
for num in range(10, 0, -1):
    print(num)

"""