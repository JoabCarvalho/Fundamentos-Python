lista = [1,2,2,5,6,31,4,9,978,25,25,4,4,5,5,5,8,12,11]
print(f"A lista é: {lista}.")
print(f"A lista ordenada é: {sorted(lista)}.")
print(f"A lista tem tamanho de {len(lista)} elementos.")
print("\n")

# Transformamos a lista em um conjunto, o que automaticamente remove os números repetidos
conjunto = set(lista)
print(f"O conjunto é: {conjunto}.")
print(f"O conjunto ordenado é: {sorted(conjunto)}.")
print(f"O conjunto tem tamanho de {len(conjunto)} elementos.")
print("\n")

listaNova = list(conjunto)
print(f"A nova lista é: {sorted(listaNova)}.")
print(f"A nova lista tem tamanho de {len(listaNova)} elementos.")