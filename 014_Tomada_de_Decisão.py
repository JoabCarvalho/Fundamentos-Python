# Estrutura IF, ELIF e ELSE

nota = 8

if nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")

print("\n")

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

frutas = ["maçã", "banana", "laranja"]

print("Frutas disponíveis:\n")

frutas = [fruta.capitalize() for fruta in frutas] # frutas recebe a fruta CAPITALIZE através do FOR IN frutas, assim terá a 1º letra maiúscula.
for fruta in frutas:
    print(f" > {fruta}")

print("\n")

formacao_dsa = {"Cientista de Dados": 6, "Analista de Dados": 4}

for curso, valor in formacao_dsa.items():
    print(f"{curso}: R$ {valor} Mil.")