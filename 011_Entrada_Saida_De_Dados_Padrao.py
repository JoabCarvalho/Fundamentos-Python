valor = 456.69987

print(f'Valor formatado com 2 casas decimais: R$ {valor:.2f}.')

nome = input('Digite seu nome: ')
idade = input('Digite a sua idade: ')
idade = int(idade)

from datetime import date
ano_atual = date.today().year
ano_nascimento = ano_atual - idade

print(f'Seu nome é {nome}, você tem {idade} anos, nasceu aproximadamente em {ano_nascimento}.')