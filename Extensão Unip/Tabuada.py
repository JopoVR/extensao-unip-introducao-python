# Programa que mostra a tabuada de um número
# Demonstra o uso de laços de repetição (for)

num = int(input("Digite um número para ver sua tabuada: "))

for i in range(1, 11):  # laço de 1 até 10
    print(f"{num} x {i} = {num * i}")
