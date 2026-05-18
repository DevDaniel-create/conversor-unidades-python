"""
Recebendo dado do usuário.

input() -> Todo tipo de dado recebido é uma string

Em Python tudo que estiver entre:
- Aspas siples:
- Aspas duplas:
- Aspas triplas:

Exemplos:
- Aspas simpes -> 'Angelina Jolie'
- Aspas duplas -> "Angelina Jolie"
- Aspas simples triplas -> '''Angelina Jolie'''

"""
# Aspas duplas triplas -> """Angelina Jolie"""
# Entrada de dados
# print('Qual seu nome?')
# nome = input() # input -> entrada de dados

nome = input('Digite seu nome? ')

# Exemplo de print 'antigo' 2.x
# print('Seja bem-vindo(a) %s' % nome)
# Exemplo de print moderno
# print("Seja bem-vindo(a) {0}".format(nome))
# Exemplo de print atual
print(f'Seja bem-vindo(a) {nome}')

# print("Qual sua idade?")
# idade = input()

idade = int(input("qual sua idade? "))
# processamento

# saida de dados
# Exemplo de print 'antigo' 2.x
# print('O %s tem %s anos' % (nome, idade))
# Exemplo de print moderno
# print("A {0} tem {1} anos".format(nome, idade))
# Exemplo de print moderno
print(f'A {nome} tem {idade} anos')

'''
# int(idade) => cast
# cast é a converção de u tipo de dado para outro
'''
print(f'A {nome} nasceu em {2025 - idade}')

