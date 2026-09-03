# Calculadora
# Nome: Italo Andrade Costa
# 03/03/2026 - Versão 1.0

# # Preenchimento
num1 = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

# Váriáveis
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: Divisão por zero"
else:
    resultado = "Operação Inválida"
print("Resultado:", resultado)