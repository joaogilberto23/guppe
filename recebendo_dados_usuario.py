"""
Recebendo dados do usuário
"""
# Entrada de dados
# print("Qual seu nome? ")
nome = input('Qual seu nome? ')

# Exemplo de print 'antigo' - 2.x
# print("Seja bem vindo(a) %s" % nome)

# Exemplo de print 'moderno' - 3.x
# print("Seja bem vindo(a) {0}" .format(nome))

# Exemplo de print 'atual' - 3.7
print(f'Seja bem vindo(a) {nome}')

# print("Qual sua idade? ")
idade = input('Qual sua idade? ')

# Saída de dados
# Exemplo de print 'antigo' - 2.x
# print("O(a) %s tem %s anos." % (nome, idade))

# Exemplo de print 'moderno' - 3.x
# print("O(a) {0} tem {1} anos." .format(nome, idade))

# Exemplo de print 'atual' - 3.7
print(f'O(a) {nome} tem {idade} anos, nasceu em {2018 - int(idade)}!')
