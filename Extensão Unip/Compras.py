# Programa que cria uma lista de compras
# Demonstra o uso de listas

compras = []  # lista vazia

while True:
    item = input("Digite um item para a lista (ou 'sair' para terminar): ")
    if item.lower() == "sair":
        break
    compras.append(item)  # adiciona item na lista

print("\nSua lista de compras:")
for produto in compras:
    print("-", produto)
