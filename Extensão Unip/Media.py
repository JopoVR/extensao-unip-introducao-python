# Programa que calcula a média de notas de um aluno
# Demonstra entrada de dados, listas e condições

notas = []

qtd = int(input("Quantas notas deseja cadastrar? "))

for i in range(qtd):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print(f"Média final: {media:.2f}")

if media >= 6:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado.")
