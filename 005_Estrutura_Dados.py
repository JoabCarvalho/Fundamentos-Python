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