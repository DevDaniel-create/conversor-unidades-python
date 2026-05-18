"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais:
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o progama.

2 - Variáeis locais:
    - Variaveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo está limitado ao bloco onde foi delcarado.

Para declarar uma variável em Python fazemos:

noome_da_variável = valor_da_variavel


Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao aribuiros o valor á mesma.

Exemplo em C:
int numero = 42

Exemplo em Java:
int numero = 42




"""

numero = 42 #Exemplo de variavel global
print(numero)
print(type(numero))

numero = 'Geek University'
print(numero)
print(type(numero))

nao_existo = 'oi'
print(nao_existo)

numero = 42

if numero > 10:
    novo = numero + 10 # A varável (novo) esta declarada dentro do bloco if. Portanto, é local.
    print(novo)

print(novo)


