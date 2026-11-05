# Script de estudo sobre tomada de decisão e estruturas de repetição em Python.
# Este arquivo demonstra como usar condicionais, laços e compreensões para resolver
# problemas simples de lógica de programação de forma clara e legível.

# Estrutura IF, ELIF e ELSE
# Aqui usamos condições para verificar se uma expressão é verdadeira ou falsa.
# Se a condição for atendida, executamos um bloco; caso contrário, seguimos para o Else.
nota = 8

if nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")

print("\n")

# Exemplo de classificação por idade, com múltiplas condições.
# O elif é executado somente quando a condição anterior for falsa.
# Isso permite criar uma cadeia de regras em ordem lógica.
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
# Essas estruturas de repetição permitem executar instruções várias vezes.
# O laço for percorre elementos de uma sequência e o while continua enquanto a condição for verdadeira.

# Lista de frutas que será processada.
frutas = ["maçã", "banana", "laranja"]

print("Frutas disponíveis:\n")

# Compreensão de lista: cria uma nova lista com cada item em formato capitalizado.
# Isso transforma "maçã" em "Maçã", "banana" em "Banana" e assim por diante.
frutas = [fruta.capitalize() for fruta in frutas]
for fruta in frutas:
    print(f" > {fruta}")

print("\n")

# Dicionário com cursos e valores em milhões.
# O método .items() retorna pares chave-valor, permitindo iterar sobre cada item do dicionário.
formacao_dsa = {"Cientista de Dados": 6, "Analista de Dados": 4}

for curso, valor in formacao_dsa.items():
    print(f"{curso}: R$ {valor} Mil.")

print("\n")

# O laço for também pode ser usado com range() para criar uma sequência numérica.
# range(1, 11) gera os números de 1 a 10.
print(f"Contagem de {list(range(1, 11))}:\n")
for numero in range(1, 11):
    print(f"Número: {numero}")

print("\n")

# O while executa enquanto a condição for verdadeira.
# Neste caso, a variável contador diminui até chegar a zero.
contador = 5

while contador > 0:
    print(f"Contagem regressiva: {contador}")
    contador -= 1

print("\nFim da contagem regressiva!")

# Verificação de paridade em uma tupla de números.
# A expressão numero % 2 == 0 verifica se o número é par (resto da divisão por 2 é zero).
print("\n")

numeros = (1, 2, 3, 4, 5)

for numero in numeros:
    if numero % 2 == 0:
        print(f"> {numero} é Par")
    else:
        print(f"> {numero} é Ímpar")

# Exemplo de decisão baseada no início do nome.
# O método startswith() verifica se a string começa com um prefixo específico.
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
# O código classifica cada produto como caro ou barato de acordo com o valor do preço.
print("\n")

produtos = {"Arroz": 5.50, "Feijão": 7.30, "Macarrão": 4.20}

for produto, preco in produtos.items():
    if preco > 6:
        print(f"> {produto} é caro: R$ {preco}")
    else:
        print(f"> {produto} é barato: R$ {preco}")

print("\n")

# Compreensão de lista.
# Cria uma nova lista com os quadrados dos números de 0 a 10.
quadrados = [x**2 for x in range(11)]
print(f"Quadrados de 0 a 10: {quadrados}.")
print(type(quadrados))

print("\n")

# Compreensão de lista com filtro.
# Aqui, apenas os números pares são incluídos na lista.
pares = [x for x in range(21) if x % 2 == 0]
print(f"Pares de 0 até 20: {pares}.")
print(type(pares))

print("\n")

# Compreensão de dicionário.
# Cada chave recebe um número e cada valor recebe o seu quadrado.
numeros_com_quadrados = {x: x**2 for x in range(11)}
print(f"Números de 0 até 10 com seus quadrados: {numeros_com_quadrados}.")
print(type(numeros_com_quadrados))

print("\n")

# Lista com valores repetidos, que serão transformados em dicionário.
# Como as chaves do dicionário precisam ser únicas, os números repetidos sobrescrevem entradas anteriores.
conjunto = [1, 2, 2, 3, 3, 4, 5, 5]
print(f"Conjunto original: \n {conjunto}.")
print(type(conjunto))
quadrados_sem_repeticao = {x: x ** 2 for x in conjunto}
print(f"Quadrados sem repetição: \n {quadrados_sem_repeticao}.")
print(type(quadrados_sem_repeticao))

print("\n")

# Gerador.
# Diferente de uma lista, o gerador produz valores sob demanda e economiza memória.
gen = (x ** 2 for x in range(11))
print(f"Gerador de quadrados de 0 a 10: {gen}.")
print(type(gen))
print("---")

# Tupla com valores gerados a partir de uma expressão.
# A tupla é imutável: depois de criada, seus valores não podem ser alterados.
quadrados_tuple = tuple(x ** 2 for x in range(11))
print(f"Quadrados de 0 a 10 em tupla: {quadrados_tuple}.")
print(type(quadrados_tuple))