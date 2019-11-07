"""
Tipo String

Em Python as strings podem vir....

- Entre aspas simples -> 'nome'
- Entre aspas dulpas -> "nome"
- Entre aspas simples triplas -> '''nome'''
- Entre aspas duplas triplas -> """ """

"""
nome = 'João Gilberto'
print(nome)
nome = "João Gilberto"
print(nome)
nome = '''João Gilberto'''
print(nome)
nome = """João Gilberto"""
print(nome)
nome = "Gina's Bar"  # Caso precise usar apóstrofo ('), usa-se as demais formas pra indicar o inicio e fim da string.
print(nome)

"""
Algumas funções
"""
print(nome.upper())  # Deixa tudo em caixa alta

print(nome.lower())  # Deixa tudo em caixa baixa

print(nome.split())  # Transforma em uma lista de strings separadas pelo espaço entre elas

print(nome[0:4])  # Imprime por posição dos vetores - Slice de string

print(nome.split()[1])  # Imprime por posição da lista - Slice de string

print(nome[::])  # Imprime da primeira até a última posição

print(nome[::-1])  # Imprime da primeira até a última posição de trás para frente


