"""
Tipo String

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre aspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''

"""
# Estiver entre aspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""

nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'  # \n serve para dar um espaço de uma linha
print(nome)
print(type(nome))

nome = 'Geek University'
print(nome.split())  # o .split() sepera como uma lista