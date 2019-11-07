"""
Tipo Float

- Separador de casas decimais é o ponto, não a vírgula. Exemplo: 25.55

- Ao converter (realizar um cast) de um número float para int, perdem-se as casas decimais, ou seja,
perde-se precisão.

"""

num = 1.45
print(num)

print(int(num))    # cast - Conversão de número float para inteiro
