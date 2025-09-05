# Programa que verifica se um número é primo
# Um número é primo se for divisível apenas por 1 e ele mesmo

num = int(input("Digite um número: "))
eh_primo = True

if num < 2:
    eh_primo = False
else:
    for i in range(2, int(num**0.5) + 1):  # só precisa ir até a raiz quadrada
        if num % i == 0:
            eh_primo = False
            break

if eh_primo:
    print(num, "é primo")
else:
    print(num, "não é primo")
