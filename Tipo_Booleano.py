"""
Tipo Booleano

Algébra booleana, George boole

2 constantes, verdadeira ou falsa

True -> Verdadeiro

False -> Falso

OBS: Sempre com a inicial maiúscula

Errado:

true, false

Certo:

True, False
"""

ativo = True
print(ativo)

"""
Operações básicas
"""

# Negação (not):
"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso.
se for falso o resultado será verdadeiro. Ou seja sempre o contrário.
"""
print(not ativo)

legado = False

# Ou (or):
"""
É uma operaração binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadadeiro

True or True -> True 
True or False -> True 
False or True -> True 
False or False -> False
"""
print(ativo or legado)

# E (and):
"""
Também é uma operação binária, ou seja, também depende de dois valores. Ambos os valores devem ser verdadeiro.

True and True -> True 
True or False -> False
False or True -> False 
False or False -> False

"""


