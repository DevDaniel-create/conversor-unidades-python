"""

15. Leia um ângulo em radianos e apresente-o convertido em graus. A formula de conversão
é: G = R * 180/pi, sendo G o angulo em graus e R em radianos e pi = 3.14.

"""

R = float(input("Digite o ângulo em radianos: "))
G = R * 180/3.14
print(f"O valor do ângulo em graus é: {G: .2f} ")  # .2f faz com que fique com no máximo 2 casas decimais.

