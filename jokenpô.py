import random


print('Olá, me chamo Z! Sou um bot programado para partidas de jokenpô! Você aceitaria este desafio?')
print('\n[ SIM ]   [ NÃO ]\n')

play_answer = input('Resposta: ').upper()

while play_answer != 'SIM' and play_answer != 'NÃO':
    print('Opa, esta não é uma marcação válida. Você deve responder apenas com <SIM> ou <NÃO>.\n')
    play_answer = input('Resposta: ')

while play_answer == 'NÃO':
    print('Tudo bem! Caso mude de ideia, pode responder com <SIM> logo abaixo. Tenho certeza de que será divertido! ^^\n\n')
    play_answer = input('Resposta: ')

while play_answer == 'SIM':

    p_wins = 0
    b_wins = 0
    options = ['pedra', 'papel', 'tesoura']

    player = input('Como posso te chamar? Insira um apelido abaixo: *max 15 caracteres\nApelido: ')

    # DEFININDO UM APELIDO PARA O JOGADOR:
    while len(player) > 15:
        print(f'<{player} não é um nome válido. Por favor, escolha um novo:')
        player = input('Apelido: ')

# DEFININDO A QUANTIDADE DE VITÓRIAS NECESSÁRIAS PARA ENCERRAR A PARTIDA:

    print(f'\nCerto, vou chamar você de {player}.\nAntes de começarmos, quantas vitórias finalizam o jogo?\nA) 1 vitória\nB) 2 vitórias\nC) 3 vitórias')
    answer = input('Resposta: ').upper()

    while answer != 'A' and answer != 'B' and answer != 'C' :
        print('Não identifiquei uma resposta válida. Vamos tentar novamente.\nCertifique-se de responder com <A>, <B> ou <C>, ok?\n\n')
        answer = input('Resposta: ').upper()
    
    if answer == 'A' :
        wins = 1
    elif answer == 'B' :
        wins = 2
    else :
        wins = 3
    
    # VARIÁVEL PARA VITÓRIAS
    if wins > 1 :
        v_wins = 'vitórias'
    else :
        v_wins = 'vitória'

    # PROGRAMANDO AS PARTIDAS

    while p_wins < wins and b_wins < wins :
        # ESCOLHA DO BOT
        b_choice = random.choice(options)

        #ESCOLHA DO JOGADOR
        print(f'\nAs partidas encerram quando um de nós completarmos {wins} {v_wins}.\nDeixe sua escolha abaixo:\n<pedra>   <papel>   <tesoura>\n')
        p_choice = input('Sua Escolha: ').lower()

        while p_choice != 'pedra' and p_choice != 'papel' and p_choice != 'tesoura':
            print(f'Ops... <{p_choice}> não é uma opção válida. Tente escolher entre <pedra>, <papel> ou <tesoura>, ok?')
            p_choice = input('Sua Escolha: ').lower()

        # CONFIRMANDO RESULTADO
        print(f'Minha Escolha: {b_choice}')

        if (p_choice == 'pedra' and b_choice == 'tesoura') or (p_choice == 'papel' and b_choice == 'pedra') or (p_choice == 'tesoura' and b_choice == 'papel') :
            print('< Muito bem, você ganhou essa. >\n')
            p_wins += 1
        elif p_choice == b_choice :
            print('< Entramos num empate. Ninguém ganha ponto dessa vez. >\n')
        else :
            print('< Eu ganhei! >\n')
            b_wins += 1

        print(f'Placar Atual:\n[{player}: {p_wins}  ]\n[Z(EU): {b_wins}  ]\n')

    print(f'Fim de Jogo!')

    if p_wins > b_wins :
        print('< Você Ganhou! >\n\n')
    else :
        print('< Eu ganhei! >\n\n')
    
    play_answer = input('Gostaria de Jogar Novamente?\n[ SIM ]   [ NÃO ]\nResposta: ').upper()