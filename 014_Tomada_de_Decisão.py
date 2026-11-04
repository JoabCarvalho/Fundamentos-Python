# Estrutura IF, ELIF e ELSE
# Este bloco mostra como usar condições para tomar decisões no programa.

# Exemplo simples de aprovação: nota maior ou igual a 7 resulta em aprovado.
nota = 8

if nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")

print("\n")

# Exemplo de classificação por idade, com múltiplas condições.
# O elif é executado quando a condição anterior for falsa.
idade = 17

if idade < 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")

# FOR e WHILE
# Estruturas de repetição usadas para percorrer listas e executar blocos várias vezes.

# Lista de frutas que será processada.
frutas = ["maçã", "banana", "laranja"]

print("Frutas disponíveis:\n")

# Compreensão de lista: cria uma nova lista com cada item capitalizado.
# Isso transforma "maçã" em "Maçã", "banana" em "Banana" e assim por diante.
frutas = [fruta.capitalize() for fruta in frutas]
for fruta in frutas:
    print(f" > {fruta}")

print("\n")

# Dicionário com cursos e valores em milhões.
# O loop percorre cada chave e valor utilizando .items().
formacao_dsa = {"Cientista de Dados": 6, "Analista de Dados": 4}

for curso, valor in formacao_dsa.items():
    print(f"{curso}: R$ {valor} Mil.")

print("\n")

# O laço for também pode ser usado com range() para criar sequência numérica.
print(f"Contagem de {list(range(1, 11))}:\n")
for numero in range(1, 11):
    print(f"Número: {numero}")

print("\n")

# O while executa enquanto a condição for verdadeira.
# Aqui, a contagem regressiva vai até zero.
contador = 5

while contador > 0:
    print(f"Contagem regressiva: {contador}")
    contador -= 1

print("\nFim da contagem regressiva!")

# Verificação de paridade em uma tupla de números.
# A expressão numero % 2 == 0 identifica números pares.
print("\n")

numeros = (1, 2, 3, 4, 5)

for numero in numeros:
    if numero % 2 == 0:
        print(f"> {numero} é Par")
    else:
        print(f"> {numero} é Ímpar")

# Exemplo de decisão baseada no início do nome.
# O método startswith() verifica o prefixo da string.
print("\n")

nomes = ["Ana", "Bruno", "Carlos", "Diana"]

for nome in nomes:
    if nome.startswith("A"):
        print(f"> {nome} começa com A")
    elif nome.startswith("B"):
        print(f"> {nome} começa com B")
    else:
        print(f"> {nome} não começa com A nem B")

# Exemplo com dicionário e comparação de preços.
# O bloco de código classifica cada produto como caro ou barato.
print("\n")

produtos = {"Arroz": 5.50, "Feijão": 7.30, "Macarrão": 4.20}

for produto, preco in produtos.items():
    if preco > 6:
        print(f"> {produto} é caro: R$ {preco}")
    else:
        print(f"> {produto} é barato: R$ {preco}")

print("\n")

quadrados = [x**2 for x in range(11)]
print(f"Quadrados de 0 a 10: {quadrados}.")
print(type(quadrados))

print("\n")

pares = [x for x in range(21) if x % 2 == 0]
print(f"Pares de 0 até 20: {pares}.")

print("\n")
