print("\n----------------------------------------\n")

numero_inteiro = 10
print(f"Valor: {numero_inteiro}, Tipo: {type(numero_inteiro)}\n")

numero_decimal = 3.14
print(f"Valor: {numero_decimal}, Tipo: {type(numero_decimal)}\n")

texto = "Eu sou um texto"
print(f"Valor: {texto}, Tipo: {type(texto)}\n")

booleano = True
print(f"Valor: {booleano}, Tipo: {type(booleano)}")

print("\n----------------------------------------\n")

print("Operadores Aritmétricos:\n")
print(f"Adição: {numero_inteiro} + {numero_decimal} = {numero_inteiro + numero_decimal}")
print(f"Subtração: {numero_inteiro} - {numero_decimal} = {numero_inteiro - numero_decimal}")
print(f"Multiplicação: {numero_inteiro} * {numero_decimal} = {numero_inteiro * numero_decimal}")
print(f"Divisão: {numero_inteiro} / {numero_decimal} = {numero_inteiro / numero_decimal}")
print(f"Divisão Inteira: {numero_inteiro} // {numero_decimal} = {numero_inteiro // numero_decimal}")
print(f"Resto da Divisão: {numero_inteiro} % {numero_decimal} = {numero_inteiro % numero_decimal}")
print(f"Exponenciação: {numero_inteiro} ** 2 = {numero_inteiro ** 2}")

print("\n----------------------------------------\n")

# Isso NÃO pode!
# 8 + "8"

# Mas isso pode! Isso é concatenação, é juntar palavras.
# "8" + "8" = "88"

# Isso também pode! Isso é repetição, é repetir a palavra.
# 8 * "8" = "88888888"

# Isso também pode! Isso é concatenação, é juntar palavras.
# "8" + "s" = "8s"

# Operadores

x = 10
y = 8

print(f"{x} > {y}  ? {x > y}")
print(f"{x} < {y}  ? {x < y}")
print(f"{x} >= {y} ? {x >= y}")
print(f"{x} <= {y} ? {x <= y}")
print(f"{x} == {y} ? {x == y}")
print(f"{x} != {y} ? {x != y}")

print("\n----------------------------------------\n")

tem_dinheiro = True
tem_tempo = False

print(f"Posso comprar? {tem_dinheiro and tem_tempo}")
print(f"Posso comprar? {tem_dinheiro or tem_tempo}")
print(f"Posso comprar? {tem_dinheiro and not tem_tempo}")