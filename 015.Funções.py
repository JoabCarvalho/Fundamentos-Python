def saudacaoDoCurso():
    """Esta função imprime uma saudação para o curso."""
    print("\nBem-vindo ao curso de Python!\n")

saudacaoDoCurso()

def somaNumeros(a, b):
    """Esta função retorna a soma de dois números."""
    return a + b

# O input() sempre retorna texto; trocamos a vírgula decimal por ponto antes de converter o texto para float.
entrada_a = input("Digite o primeiro número: ")
a = float(entrada_a.replace(",", "."))

entrada_b = input("Digite o segundo número: ")
b = float(entrada_b.replace(",", "."))

soma = somaNumeros(a, b)
print(f"A soma de {entrada_a} e {entrada_b} é {soma}.")

print("\n")