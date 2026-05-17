"""
Tipo Float

Tipo real, decimal

casas decimais

OBS: O separardor de casas decimais é o . e nao a ,;


"""

# Errado do ponto de vista do float, mas gera uma tupla
valor = 1, 44
print(valor)
print(type(valor))

# certo do ponto de vista do float
valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float para um int.
"""
OBS: Ao coverter um float para um int perdemos precisão.
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com numeros complexos

variavel = 5j

print(variavel)