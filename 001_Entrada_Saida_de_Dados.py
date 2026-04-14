# Programa que lê duas notas e calcula a média delas

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print(f"A média da soma das notas {nota1} + {nota2} é: {media}!")

if media >= 6:
    print("Parabéns, você passou!")
else:
    print("Infelizmente você não passou, estude mais para a próxima prova!")


# Declaração de variáveis e atribuição de valores

nome = "João"           # String
idade = 35              # Inteiro
altura = 1.78           # Float
estudante = True        # Boolean

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Altura: {altura}")
print(f"É estudante: {estudante}")