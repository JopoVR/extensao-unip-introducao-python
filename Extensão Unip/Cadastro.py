# Programa que cadastra alunos com nome e idade
# Demonstra o uso de dicionários

alunos = []

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para terminar): ")
    if nome.lower() == "sair":
        break
    idade = int(input("Digite a idade: "))
    aluno = {"nome": nome, "idade": idade}
    alunos.append(aluno)

print("\nLista de alunos cadastrados:")
for a in alunos:
    print(f"Nome: {a['nome']}, Idade: {a['idade']}")
