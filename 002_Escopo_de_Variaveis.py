# Variável Global

saudacao = "Olá, sejam bem-vindo ao curso de Python!"
nome = "Maria"


def minha_funcao():
    # Variável Local
    nome = "João"
    print(f"\nDentro da função:{nome}.")
    print(f"\nAcessando a variável global de dentro da função: {saudacao}.")

minha_funcao()

print(f"\nFora da função: {nome}.")
print(f"\nAcessando a variável global de fora da função: {saudacao}.")