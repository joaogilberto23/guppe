"""
O BREAK funciona da mesma forma que em C ou Java, por exemplo,
é utilizado para sair de loops de maneira projetada.

# Exemplo 1

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('Sai do loop!')

# Exemplo 2

while True:
    comando = input("Digite 'sair' para sair: ")
    if comando == 'sair':
        break

"""