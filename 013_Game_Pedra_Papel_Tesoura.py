print('------------------------------------------------------------')
print('*****         O JOGO "PEDRA vs PAPEL vs TESOURA"       *****')
print('------------------------------------------------------------')
print('***              DESCRIÇÃO E REGRAS DO JOGO              ***')
print('------------------------------------------------------------')
print('*   1. Pedra VENCE Tesoura, mas PERDE para Papel.          *')
print('*   2. Papel VENDE Pedra, mas PERDE para Tesoura.          *')
print('*   3. Tesoura VENCE Papel, mas PERDE para Pedra.          *')
print('*   4. Se as escolhas forem iguais, o jogo fica empatado.  *')


while True:
    print('------------------------------------------------------------')
    print('Escolha uma das opções abaixo: \n 1 - Pedra \n 2 - Papel \n 3 - Tesoura \n')
    jogador1 = input('Faça sua escolha Jogador 1: ')

    if jogador1.lower() not in ['1', '2', '3', 'pedra', 'papel', 'tesoura']:
        print('------------------------------------------------------------')
        print('Opção inválida Jogador 1! Escolha direito, sua vitória depende disso!!!')
        print('Por favor, escolha entre 1, 2 ou 3.')
        continue
    else:
        break


while True:
    print('------------------------------------------------------------')
    jogador2 = input('Faça sua escolha Jogador 2: ')
    if jogador2.lower() not in ['1', '2', '3', 'pedra', 'papel', 'tesoura']:
        print('------------------------------------------------------------')
        print('Opção inválida Jogador 2! Escolha direito, sua vitória depende disso!!!')
        print('Por favor, escolha entre 1, 2 ou 3.')
        continue
    else:
        break


if jogador1.lower() in ['1', 'pedra']:
    jogador1 = 'Pedra'

elif jogador1.lower() in ['2', 'papel']:
    jogador1 = 'Papel'

elif jogador1.lower() in ['3', 'tesoura']:
    jogador1 = 'Tesoura'


if jogador2.lower() in ['1', 'pedra']:
    jogador2 = 'Pedra'

elif jogador2.lower() in ['2', 'papel']:
    jogador2 = 'Papel'

elif jogador2.lower() in ['3', 'tesoura']:
    jogador2 = 'Tesoura'


vencedor = None

if jogador1 == jogador2:
    vencedor = 'Empate'
    print('------------------------------------------------------------')
    print(f'O jogo deu {vencedor}!\nTentem novamente se não gostaram do resultado!')
    print('------------------------------------------------------------')
else:
    # Determinar o vencedor com base nas regras do jogo
    if (jogador1 == 'Pedra' and jogador2 == 'Tesoura') or \
       (jogador1 == 'Papel' and jogador2 == 'Pedra') or \
       (jogador1 == 'Tesoura' and jogador2 == 'Papel'):
        vencedor = 'Jogador 1'
        print('------------------------------------------------------------')
        print(f'O vencedor é o {vencedor}!\nParabéns!')
        print('------------------------------------------------------------')
    else:
        vencedor = 'Jogador 2'
        print('------------------------------------------------------------')
        print(f'O vencedor é o {vencedor}!\nParabéns!')
        print('------------------------------------------------------------')