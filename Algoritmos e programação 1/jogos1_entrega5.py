import random

'''
1) Esse é o jogo dos dados, muito usado em Las Vegas nos cassinos, aposte em um
número que seja o resultado da soma deles e ganhe o seu dinheiro. Crie duas variáveis
para representar os dados e uma para sua aposta, crie uma para armazenar o
resultado e faça a verificação.
'''
coins=100



def roll_Dice():
    return random.randint(1,6)

def verificate_Number(min,max):
    player_Number=(input(f"Qual número, dentro do intervalo [{min},{max}], você gostaria de apostar? ")).strip()
    while player_Number=='' or int(player_Number)<min or int(player_Number)>max:
        print('Valor informado fora do intevalo')
        player_Number=(input(f"Qual número, dentro do intervalo [{min},{max}], você gostaria de apostar? ")).strip()
    return int(player_Number)


def verificate_Bet(coins):
    player_Bet=(input(f"Quanto, dentro do intervalo[1,{coins}], você gostaria de apostar? ")).strip()
    while player_Bet=='' or int(player_Bet)<1 or int(player_Bet)>coins:
        print('Valor informado fora do intevalo')
        player_Bet=(input(f"Quanto, dentro do intervalo[1,{coins}], você gostaria de apostar? ")).strip()
    return int(player_Bet)

def play():
    global coins

    dice_One=roll_Dice()
    dice_Two=roll_Dice()
    

    player_Number= verificate_Number(1,12)
    player_Bet=verificate_Bet(coins)
    
    print('O valor da soma dos dados foi ',dice_Two+dice_One)
    if player_Number==(dice_One+dice_Two):
        print('Parabéns, você ganhou!!!!')
        coins=coins+player_Bet
        print(f"Você tem {coins} coins")
    else:
        print("Espero que ganhe na próxima")
        coins=coins-player_Bet
        print(f"Você tem {coins} coins")
    


def keep_playing():
    global coins
    while True:
        
        if coins<=0:
            
            print('FIM DE JOGO. Você ficou sem coins!!!!')
            answer=input('Você deseja jogar novamente? [S/N]: ')
            if answer.upper()=='N':
                break
            else:
                coins=100
        if coins>0:
            play()
            
        
        

keep_playing()