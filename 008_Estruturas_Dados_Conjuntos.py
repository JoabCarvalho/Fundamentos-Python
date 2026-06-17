# Conjuntos são uma coleção de itens únicos e não ordenados. Eles são úteis para armazenar elementos distintos e realizar operações matemáticas como união, interseção e diferença.

# Criando um conjunto
conjunto_a = {1,2,3,2,4,5,6,3,4,8,9,1,2,10}
print(conjunto_a)

# Qual número de 1 a 10 não está presente no conjunto_a?
numeros_de_1_a_10 = set(range(1,11))
numeros_faltando = numeros_de_1_a_10 - conjunto_a
print(f"Números de 1 a 10 que não estão presentes no conjunto_a é: \"{numeros_faltando}\".")

adicionar_numero = input("Deseja adicionar um número ao conjunto A? (Sim ou Não): ")

# Se adicionar número for Sim ou Não
while adicionar_numero.lower() not in ["s","sim","y","yes","n","não","no"]:
    adicionar_numero = input("Deseja adicionar um número ao conjunto A? Responda Sim ou Não: ")

print("\n")

# Se adicionar número for Sim, pergunta qual número
if adicionar_numero.lower() in ["s","sim","y","yes"]:
    numero_para_adicionar = input("Digite o número que deseja adicionar ao conjunto A: ")
    while not numero_para_adicionar.isdigit():
        print(f"O valor digitado \"{numero_para_adicionar}\" não é um número válido.")
        numero_para_adicionar = input("Digite o número que deseja adicionar ao conjunto A: ")
    # Adiciona ao conjunto
    conjunto_a.add(int(numero_para_adicionar))
    # Imprime na tela o número adicionado e o conjunto atualizado
    print(f"O número {numero_para_adicionar} foi adicionado ao conjunto A. O conjunto A agora é: {conjunto_a}.")
else:
    print("Nenhum número foi adicionado ao conjunto A.")

print("\n")

# Pergunta se deseja remover algum número do conjunto A
remover_numero = input("Deseja remover um número do conjunto A? (Sim ou Não): ")

# Verifica se a resposta até que seja Sim ou Não ("s","sim","y","yes","n","não","no")
while remover_numero.lower() not in ["s","sim","y","yes","n","não","no"]:
    remover_numero = input("Deseja remover um número do conjunto A? Responda Sim ou Não:")

print("\n")

# Se remover número for Sim perunta qual número e remove do conjunto A
if remover_numero.lower() in ["s","sim","y","yes"]:
    print("Digite o número que deseja remover do conjunto A.")
    print(f"Lembre-se de que o conjunto A é: {conjunto_a}!")
    numero_para_remover = input("Número para remover: ")

    # Verifica o número para remover até que seja um número válido e esteja presente no conjunto A
    while not numero_para_remover.isdigit() or int(numero_para_remover) not in conjunto_a:
        print(f"O número digitado \"{numero_para_remover}\" não é um número válido ou não está presente no conjunto A.")
        print(f"O conjunto A é: {conjunto_a}.")
        numero_para_remover = input("Número para remover: ")
    
    # Transforma o TEXTO em INTEIRO e remove do conjunto A. 
    # conjunto_a.discard(int(numero_para_remover))
    conjunto_a.remove(int(numero_para_remover))
    print("\n")
    print(f"O número \"{numero_para_remover}\" foi removido do conjunto A.")
    print(f"O conjunto A agora é: {conjunto_a}.")
else:
    print("Nenhum número foi removido do conjunto A.")