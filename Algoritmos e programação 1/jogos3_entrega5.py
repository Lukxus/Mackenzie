'''
3) Um dos jogos sugeridos para crianças acima de 6 anos é o PEDRA, PAPEL E TESOURA
Como jogar:
Dois participantes ficam um de frente para o outro e, ao mesmo tempo, jogam uma
das mãos para frente representando um dos três símbolos: pedra (mão fechada), papel
(mão aberta) ou tesoura (dedos indicador e médio estendidos).
Para definir o vencedor segue-se a seguinte regra: pedra ‘quebra’ a tesoura; tesoura
‘corta’ o papel e papel ‘embrulha’ a pedra. Se ambas escolhem a mesma, há empate.
Este jogo também chama-se Joquempô, jo-quem-pô.
Sabendo como funciona o jogo crie uma variável para cada jogador que deve
armazenar a opção escolhida pela criança (Pedra, Papel ou Tesoura) e apresente o
resultado da jogada.
'''

import random

coins=100

def roll_Luck():
    return random.randint(1,3)

def possible_Moves(move):
    if move==1:
        return "PEDRA"
    if move==2:
        return "PAPEL"
    if move==3:
        return "TESOURA"


def verificate_Number(min,max):
    player_Number=input(f"Qual será a sua jogada? ")
    while player_Number=='' or int(player_Number)<min or int(player_Number)>max:
        print('Valor informado fora do intevalo')
        player_Number=input(f"Qual será a sua jogada? ")
    return int(player_Number)

comp_Points=0
player_Points=0
def keep_playing():
    global player_Points
    global comp_Points
    while True:
        print("Digite [1] para Pedra; [2] para Papel; 
    [3] para tesoura.")
        comp_Move=roll_Luck()
        comp_Move=possible_Moves(comp_Move)
        player_Choice=verificate_Number(1,3)
        player_Choice=possible_Moves(player_Choice)
        print('O computador jogou',comp_Move)
        print('Você jogou',player_Choice)
        if player_Choice[0:2]=="PE" and comp_Move[0:2]=='TE':
            print('Parabéns você ganhou!!!!!!')
            player_Points=player_Points+1
        elif player_Choice[0:2]=="PA" and comp_Move[0:2]=='PE':
            print('Parabéns, você ganhou!!!!')
            player_Points=player_Points+1
        elif player_Choice[0:2]=='TE' and comp_Move[0:2]=='PA':
            print('Parabéns, você ganhou!!!!')
            player_Points=player_Points+1
        elif player_Choice[0:2]=='PE' and comp_Move[0:2]=='PE':
            print("Empate!!Espero que ganhe na próxima")
        elif player_Choice[0:2]=='PA' and comp_Move[0:2]=='PA':
            print("Empate!!Espero que ganhe na próxima")
        elif player_Choice[0:2]=='TE' and comp_Move[0:2]=='TE':
            print("Empate!!Espero que ganhe na próxima")
        elif player_Choice[0:2]=='PE' and comp_Move[0:2]=='PA':
            print("PERDEU!!Espero que ganhe na próxima")
            comp_Points=comp_Points+1
        elif player_Choice[0:2]=='TE' and comp_Move[0:2]=='PE':
            print("PERDEU!!Espero que ganhe na próxima")
            comp_Points=comp_Points+1
        elif player_Choice[0:2]=='PA' and comp_Move[0:2]=='TE':
            print("PERDEU!!Espero que ganhe na próxima")
            comp_Points=comp_Points+1
        print(f"Você fez {player_Points} pontos")
        print(f"O computador fez {comp_Points} pontos")
        
        print('_._'*30)
        answer=input('Você deseja jogar novamente? [S/N]: ')
        print('')
        print('_._'*30)
        if answer.upper()=='N':
            break                

keep_playing()
print("BOM JOGO!!!!")