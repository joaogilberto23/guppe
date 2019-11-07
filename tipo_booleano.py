"""
Tipo Booleano

True or False, sempre com iniciais maiúsculas.
"""
ativo = True
logado = False

print(ativo)  # True
print(logado)  # False

"""
Operações básicas:
"""
# Negação (not)
print(not ativo)  # False

# OU (or) - um dos valores deve ser verdadeiro para retornar True
"""
True or True   -> True
True or False  -> True
False or True  -> True
False or False -> False
"""
print(ativo or logado)  # True or False -> True
print(not ativo or logado)  # False or False -> False

# E (and) - ambos os valores devem ser verdadeiro para retornar True
"""
True and True   -> True
True and False  -> False
False and True  -> False
False and False -> False
"""
print(ativo and logado)  # True and False -> False
print(ativo and not logado)  # True and True -> True
