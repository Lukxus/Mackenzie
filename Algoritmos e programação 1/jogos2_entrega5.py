'''
2) O Jogo do par ou ímpar é usado onde duas pessoas jogam geralmente para decidir
um impasse, cada um escolhe entre par ou ímpar e mostra o seu número, a soma
entre eles resulta em um número par ou ímpar e assim é decidido o vencedor. Aqui
faremos com a máquina, ela escolherá um número randômico entre 0 e 10 e você
escolherá o seu.
Vamos ver quem é o vencedor!!!!

'''

import random
points=0

def roll_Number():
    return random.randint(0,10)

def verificate_Number(min,max):
    player_Number=(input(f"Quantos dedos você irá jogar?[{min},{max}]: ")).strip()
    while player_Number=='' or int(player_Number)<min or int(player_Number)>max:
        print('Valor informado fora do intevalo')
        player_Number=(input(f"Quantos dedos você irá jogar?[{min},{max}]: ")).strip()
    return int(player_Number)


def play():
    player_Number= verificate_Number(0,10)
    comp=roll_Number()
    sum_Value=(player_Number+comp)%2
    print(f"O computador jogou {comp}")
    if sum_Value==0:
        print(f"O número final é {sum_Value}, que é par!!")
        return 'P'
    else:
        print(f"O número final é {sum_Value}, que é ímpar!!")
        return "I"
        
def choice ():
    player_Choice=input("Voce deseja Par um Impar?[P/I] :").upper().strip()[0]
    while player_Choice[0] not in 'PI':
        print('Essa opção não está disponível.')
        player_Choice=input("Voce deseja Par um Impar?[P/I] :").upper().strip()
    return player_Choice[0]

def keep_playing():
    while True:
        global points
        player_Choice=choice()
        match_Result=play()
        if player_Choice==match_Result:
            print('Parabéns, você ganhou!!!!')
            points=points+1
        else:
            print("Espero que ganhe na próxima")
            
        answer=input('Você deseja jogar novamente? [S/N]: ')
        if answer.upper()=='N':
            print(f"Você fez {points} ponto(s).")
            break                

keep_playing()