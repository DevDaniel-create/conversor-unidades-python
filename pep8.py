"""
PEP8 - Python Enchancemente Proposal

São propostas de melhorias para a linguagem python

The Zen of python

import this

A ideia do PEP8 é que possamos escrever códigos Python em forma Pythônica.

[1] Utilize Camel Cases para nome de classes;

class Calculadora:
    pass


class CalculadoraCientifca:
    pass

[2] Utilize nomes em minúsculo, separados por underline para funções ou variáveis;

def soma():
    pass

def soma_dois():
     pass

numero = 4

numero_impar = 5

[3] Utilize 4 espaços para identação! (NÃO use tab)

if 'a' in 'banana':
    print('tem')

[4] Linhas em branco; O Python espera 2 linhas em branco
- separar funções e definições de classe com 2 linhas em branco;
- metódos dentro de uma classe devem ser separados por uma única linha em branco;

[5] -imports
-imports devem ser sempre feitos  em linhas sepradas;

# Import Errado

import sys,os

# Import Certo

import sys
import os

# nao há problema em utilizar:

from Types import StringType, ListType

#caso tenha muitos imports de um mesmo pacote, recomenda-se:

from Types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# imports devem ser colocados logo no começo do arquivo,logo depois de quaisquer outro comentário ou docstring e
# antes de constantes ou variáveis globais.

# espaços em expressões e instruções

#não faça:

funcao( algo[ 1 ], { outro: 2 } ])

#faça isso:

funcao(algo[1], {outro: 2})

#não faça:

algo (1)

#faça:

algo(1)

# Termine sempre uma instrução com uma nova linha em branco
"""
