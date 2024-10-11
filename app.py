# Função pra calcular a função do primeiro grau no python. 

# Recebe os valores de 'a' e 'b' fo usuário
a = float(input("Digite o valor de 'a': "))
b = float(input("Digite o valor de 'b': "))

def calcular_funcao(a,b):
    if a != 0:
        x = -b/a
        return x
    else:
        return "O valor de 'a' não pode ser zero."

# Chamando a função pra calcular o valor de 'x'
resultado = calcular_funcao(a,b)

# Resultado
print(f"O valor de 'x' é {resultado}")

