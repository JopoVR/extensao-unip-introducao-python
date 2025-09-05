# Programa que faz operações matemáticas básicas
# O usuário digita dois números e escolhe a operação

# Entrada de dados
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Digite sua opção: "))

# Processamento e saída
if opcao == 1:
    print("Resultado:", num1 + num2)
elif opcao == 2:
    print("Resultado:", num1 - num2)
elif opcao == 3:
    print("Resultado:", num1 * num2)
elif opcao == 4:
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("Erro: divisão por zero")
else:
    print("Opção inválida!")
