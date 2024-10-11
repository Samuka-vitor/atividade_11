# Função pra calcular a função do primeiro grau no python. 

# Recebe os valores de 'a' e 'b' fo usuário
a = float(input("Digite o valor de 'a': "))
b = float(input("Digite o valor de 'b': "))

def calcular_funcao(a,b):
        x = -b/a
        return x

# Chamando a função pra calcular o valor de 'x'
resultado = calcular_funcao(a,b)

# Resultado
print(f"O valor de 'x' é {resultado}")

