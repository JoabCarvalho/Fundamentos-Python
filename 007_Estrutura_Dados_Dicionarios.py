# Dicionários de Dados
pessoa = {
    "nome": "João",
    "idade": 30,
    "naturalidade": "Paraíba",
    "dt_nascimento": "1996-05-15",
    "cliente_ativo": True,
    "curso": ["Python", "SQL"]
}

print(pessoa)

print(type(pessoa))

print(f"O nome da pessoa é: {pessoa['nome']}.")

print(f"{pessoa['nome']} é estudante do curso {pessoa['curso']}.")

print(f"Dicionário antes de adicionar a chave profissao.")

# Adicionando um novo par chave-valor ao dicionário
pessoa["profissao"] = "Analista de Dados"
print(f"O dicionário de pessoa após adicionar a chave 'profissao' é: {pessoa}.")