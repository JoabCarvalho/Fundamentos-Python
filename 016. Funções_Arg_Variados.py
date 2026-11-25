def somarNumeros(*args):
    total = 0

    for i in args:
        total += i
    return str(total).replace(".", ",")


while True:
    try:
        quantidade = int(input("Quantos números você deseja somar: "))
        break
    except ValueError:
        print("Digite uma quantidade de número válido para a soma.") 
        print("\n")


numeros = []


for i in range(quantidade):
    while True:
        try:
            numero = float((input(f"Digite o {i + 1}º número: ")).replace(",", "."))
            numeros.append(numero)
            break
        except ValueError:
            print("Digite um número válido.")

print(f"A soma dos números é: {somarNumeros(*numeros)}")