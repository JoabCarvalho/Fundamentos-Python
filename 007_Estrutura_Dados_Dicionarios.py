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

print("\n")

print(f"O nome da pessoa é: {pessoa['nome']}.")
print(f"A idade de {pessoa.get('nome')} é: {pessoa.get('idade')}.")
print(f"{pessoa['nome']} é estudante do curso {pessoa['curso']}.")

print("\n")

print(f"Dicionário antes de adicionar a chave profissao.")
print(pessoa)

print("\n")

# Adicionando um novo par chave-valor ao dicionário
pessoa["profissao"] = "Analista de Dados"
print(f"O dicionário de pessoa após adicionar a chave 'profissao' é: {pessoa}.")

print("\n")

# Modificando o valor da profissão
modificar_profissao = input(f"Deseja modificar a profissão de {pessoa.get('nome')}?\n(Sim ou Não): ")
while modificar_profissao.lower() not in ["s", "sim", "y", "yes", "n", "não", "no"]:
    modificar_profissao = input(f"Deseja modificar a profissão de {pessoa.get('nome')}? Responda Sim ou Não: ")
    
if modificar_profissao.lower() in ["s", "sim", "y", "yes"]:
    nova_profissao = input(f"Alterar profissão \"{pessoa.get('profissao')}\" para? ")
    pessoa['profissao'] = nova_profissao
    print(f"A profissão de {pessoa.get('nome')} foi alterada para {pessoa.get('profissao')}!")

print("\n")

deletar_item_do_dicionario = input(f"Deseja deletar algum item do dicionário?\n(Sim ou Não): ")
while deletar_item_do_dicionario.lower() not in ["s","sim","y","yes","n","não","no"]:
    deletar_item_do_dicionario = input(f"Deseja deletar algum item do dicionário? Responda Sim ou Não: ")

print("\n")

if deletar_item_do_dicionario.lower() in ["s","sim","y","yes"]:
    # Mostra as chaves do dicionário para o usuário tomar conhecimento
    print(f"As chaves do dicionário são: {list(pessoa.keys())}.")
    chave_para_deletar = input("Digite a chave (item) que deseja deletar do dicionário: ")

    # Verifica se a chave digitada existe no dicionário
    while chave_para_deletar not in pessoa.keys():
        print(f"A chave digitada \"{chave_para_deletar}\" não existe no dicionário.\nAs chaves existentes são: {list(pessoa.keys())}.")
        chave_para_deletar = input("Digite a chave (item) que deseja deletar do dicionário: ")

    print("\n")

    confirmar_delecao_chave = input(f"Tem certeza que deseja deletar a chave \"{chave_para_deletar}\" do dicionário? (Sim ou Não): ")
    while confirmar_delecao_chave.lower() not in ["s","sim","y","yes","n","não","no"]:
        confirmar_delecao_chave = input(f"Tem certeza que deseja deletar a chave \"{chave_para_deletar}\" do dicionário? (Sim ou Não): ")

    if confirmar_delecao_chave.lower() in ["s","sim","y","yes"]:
        del pessoa[chave_para_deletar]
        print(f"Chave \"{chave_para_deletar}\" deletada com sucesso!")

    else:
        print(f"A chave \"{chave_para_deletar}\" não foi deletada.")