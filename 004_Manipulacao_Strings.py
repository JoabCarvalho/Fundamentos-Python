
# Define variável com uma string com espaços em branco no início e no final
frase = " Aprender Python é muito divertido! "

nome = "João"
saudacao = "Olá, " + nome + "!"
print(saudacao)

print("\n")

# Concatenação de strings usando f-strings
print(f"O tamanho da frase '{frase}' é: {len(frase)} caracteres.")

# Verificar se a frase começa ou termina com espaços em branco
print(f"Existe espaços em branco no início e no final da frase? Início: {frase.startswith(' ')}. No final: {frase.endswith(' ')}.")

# Remover os espaços em branco do início e do final da frase
frase_sem_espacos = frase.strip()
print(f"Tamanho da frase (agora sem espaços) é de: {len(frase_sem_espacos)} caracteres.")

print("\n")

print(f"{frase_sem_espacos.lower()}")
print(f"{frase_sem_espacos.upper()}")
print(f"{frase_sem_espacos.title()}")

print("\n")

print(f"Substituindo a palavra 'divertido' por 'incrível': {frase_sem_espacos.replace('divertido', 'incrível')}")
print(f"{frase_sem_espacos}")

print("\n")

# Fatiamento de strings - Indexação
print(f"A primeira letra da frase é o Index 0: {frase_sem_espacos[0]}.\n")
print(f"A primeira plavra 'Python' está na posição/Index 9 a 14: {frase_sem_espacos[9:15]} [9:15], o 15 é EXCLUSIVO.")
