# Pedimos o número pela primeira vez
numeroTexto = input("Digite um número: ")

# Criamos uma variável para controlar se o número é válido ou não
numero_valido = False

# O while vai continuar rodando ENQUANTO o número NÃO for válido
while not numero_valido:
    try:
        # Tentamos transformar o texto em um número decimal (float)
        # O float aceita tanto "5" quanto "5.5"
        numero_final = float(numeroTexto)

        # Se o Python conseguiu transformar sem erro, avisamos que o número é válido!
        numero_valido = True

    except ValueError:
        # Se o Python não conseguiu transformar (ex: o usuário digitou "abc"),
        # ele entra neste bloco 'except' em vez de quebrar o programa.
        print(f'O valor digitado "{numeroTexto}" não é um número válido.')
        print("\n")

        # Pedimos para o usuário digitar novamente para tentar de novo
        numeroTexto = input("Digite um número: ")

# Quando o 'while' terminar, significa que temos um número correto!
print(f"Sucesso! O número digitado foi: {numero_final}")
print(f"O tipo dele agora é: {type(numero_final)}")