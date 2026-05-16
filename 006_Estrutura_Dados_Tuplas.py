# Tuplas "()" NÃO SÃO MUTÁVEIS, ou sejam, não podem ser alteradas depois de criadas.
coordenadas = (10.2,20.56)
dias_semana = ("Domingo", "Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado")

print(f"Esta é a Tuplas de Coordenadas: {coordenadas}.")
print(f"O tipo de dados da variável coordenadas é: {type(coordenadas)}.")

print("\n")

print(f"Esta é a Tuplas de Dias da Semana: {dias_semana}.")

print("\n")

print(f"O dado contido na primeira posição (que inicia por 0) da tupla dias_semana é: {dias_semana[0]}.")

print("\n")

# Modificando valor na Tupla (isso não é possível, pois as tuplas são imutáveis)
# dias_semana[0] = "Domingo-Feira"

deletar_tupla_dias_semana = input("Deseja deletar a Tupla de Dias da Semana? (Sim ou Não): ")
while deletar_tupla_dias_semana.lower() not in ["s","sim","y","yes","n","não","no"]:
    deletar_tupla_dias_semana = input("Digite Sim ou Não: ")

if deletar_tupla_dias_semana.lower() in ["s","sim","y","yes"]:
    confirmacao = input("Tem certeza que deseja prosseguir em deletar a Tupla? (Sim ou Não): ")
    while confirmacao.lower() not in ["s","sim","y","yes","n","não","no"]:
        confirmacao = input("Digite Sim ou Não: ")

    if confirmacao.lower() in ["s","sim","y","yes"]:
        del dias_semana
        print("A Tupla de Dias da Semana foi deletada.")
    else:
        print("A Tupla de Dias da Semana não foi deletada.")
else:
    print("A Tupla de Dias da Semana não foi deletada.")
