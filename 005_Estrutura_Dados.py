# Listas "[]" são MUTÁVEIS
frutas = ["Amora", "Banana", "Kiwi", "Laranja", "Maçã", "Melancia", "Morango", "Pera", "Uva", "Caju"]
print(f"Lista de frutas: {frutas}")

# Tipo de dado da variável frutas
print(type(frutas))

# Acessando elementos da lista por indexação
print(f"Primeira fruta da lista: {frutas[0]}, [0].")
print(f"Última fruta da lista: {frutas[-1]}, [-1].")
print(f"A anterior à última fruta da lista: {frutas[-2]}, [-2].")
print(f"De Kiwi a Melancia: {frutas[-8:-4]}, [-8:-4].")
print(f"De Kiwi a Melancia: {frutas[2:-4]}, [2:-4].")

print("\n")

# Adicionando um elemento "Abacaxi" à lista de frutas
frutas.append("Abacaxi")

print(f"Lista de frutas após adicionar Abacaxi: {frutas}")

# Ordenando a lista de frutas em ordem alfabética
frutas.sort()
print(f"Lista de frutas ordenada: {frutas}")

print("\n")

# Deletando um elemento da lista de frutas
deletar_fruta = input("Digite o nome de uma fruta para deletar da lista: ")
if deletar_fruta in frutas:
    print(f"Existe a fruta \"{deletar_fruta}\" na lista de frutas.")
    frutas.remove(deletar_fruta)
    print(f"Lista de frutas após deletar \"{deletar_fruta}\": {frutas}")
else:
    print(f"Não existe a fruta \"{deletar_fruta}\" na lista de frutas.")

print("\n")

# Modificando um elemento da lista de frutas
modificar_fruta = input("Digite o nome de uma fruta para modificar na lista: ")
if modificar_fruta in frutas:
    print(f"A fruta \"{modificar_fruta}\" existe em sua lista de frutas.")
    index_fruta_in_frutas = frutas.index(modificar_fruta)
    nova_fruta = input(f"Deseja modificar a fruta \"{modificar_fruta}\" para qual fruta? ")

    while nova_fruta in frutas:
        print(f"A fruta \"{nova_fruta}\" já existe em sua lista de frutas.")
        nova_fruta = input(f"Deseja modificar a fruta \"{modificar_fruta}\" para qual fruta? ")
    
    frutas[index_fruta_in_frutas] = nova_fruta
    print(f"Lista de frutas após modificar \"{modificar_fruta}\" para \"{nova_fruta}\": {frutas}")
else:
    print(f"A fruta \"{modificar_fruta}\" não existe em sua lista de frutas.")

print("\n")

deletar_lista_frutas = input("Deseja deletar a lista de frutas? ")
while deletar_lista_frutas.lower() not in ["s", "sim", "y", "yes", "n", "não", "no"]:
    deletar_lista_frutas = input("Deseja deletar a lista de frutas? Responda Sim ou Não!")

if deletar_lista_frutas.lower() in ["s", "sim", "y", "yes"]:
    del frutas
    print("Lista de frutas deletada.")
if deletar_lista_frutas.lower() in ["n", "não", "no"]:
    print("Lista de frutas mantida.")