# Define uma função que apresenta uma saudação fixa.
def saudacaoDoCurso():
    """Esta função imprime uma saudação para o curso."""
    print("\nBem-vindo ao curso de Python!\n")

# Executa a função saudacaoDoCurso().
saudacaoDoCurso()

# Define uma função que recebe dois números e retorna a soma.
def somaNumeros(a, b):
    """Esta função retorna a soma de dois números."""
    return a + b

# O input() sempre retorna texto; trocamos a vírgula decimal por ponto antes de converter o texto para float.
entrada_a = input("Digite o primeiro número: ")
a = float(entrada_a.replace(",", "."))

entrada_b = input("Digite o segundo número: ")
b = float(entrada_b.replace(",", "."))

# Chama a função somaNumeros() e exibe o resultado.
soma = somaNumeros(a, b)
print(f"A soma de {entrada_a} e {entrada_b} é {soma}.")

print("\n")

# Define uma função com um parâmetro opcional chamado mensagem.
def saudacaoPersonalizada(nome, mensagem = 'Olá'):
    print(f'{mensagem}, {nome}!')

# Como mensagem não foi informada, usa o valor padrão "Olá".
saudacaoPersonalizada('João')
print("\n")
# Neste caso, a mensagem "Bem-vinda" é informada explicitamente.
saudacaoPersonalizada('Maria', 'Bem-vinda')

