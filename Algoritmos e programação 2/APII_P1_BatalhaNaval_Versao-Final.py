'''
Entrega da Prova 1: Jogo Batalha Naval - Algoritmos e Programação II
Nós,
Fabio Domingues Pereira Sabino
Luiz Octavio Tassinari Saraiva
declaramos que
todas as respostas são fruto de nosso próprio trabalho,
não copiamos respostas de colegas externos à equipe,
não disponibilizamos nossas respostas para colegas externos ao grupo e
não realizamos quaisquer outras atividades desonestas para nos beneficiar
ou prejudicar outros.
'''


import random
lista_letras=['A','B','C','D','E','F','G','H','I','J']


def inicializarGrid(): # Cria uma matriz de acordo com o jogo ||10X10
    grid=[]
    global lista_letras
    for i in range(11):
        linha=[]
        for j in range(11):
            linha.append('.')
        grid.append(linha)
    for i in range(len(lista_letras)):
        grid[i+1][0]=f'{lista_letras[i]}'
    for j in range(1,11):
        grid[0][j]=f'{j-1}'
    return grid


def imprimir(grid): #Imprime a matrix na forma de um tabuleiro
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end='    ')
        print()


def posicionar_porta_avioes(grid, linha, coluna, vertical): #Posiciona o barco porta-aviões
    global lista_letras
    linha=lista_letras.index(linha)+1
    if vertical==True:
        for i in range(0,5):
            if grid[linha+i][coluna]=="." and (linha+5)<=10:
                grid[linha+i][coluna]='P'
            else:
                return False
    elif vertical==False:
        for j in range(0,5):
            if grid[linha][coluna+j]=="." and (coluna+5)<=10:
                grid[linha][coluna+j]='P'
            else:
                return False
    return True


def posicionar_encouracado(grid, linha, coluna, vertical): #Posiciona o barco encouraçado
    global lista_letras
    linha=lista_letras.index(linha)+1
    if vertical==True:
        for i in range(0,4):
            if grid[linha+i][coluna]=="." and (linha+4)<=10:
                if i==3:
                    grid[linha+i][coluna]='E'
                    grid[linha+i-1][coluna]='E'
                    grid[linha+i-2][coluna]='E'
                    grid[linha+i-3][coluna]='E'
            else:
                return False
    elif vertical==False:
        for j in range(0,4):
            if grid[linha][coluna+j]=="." and (coluna+4)<=10:
                if j==3:
                    grid[linha][coluna+j]='E'
                    grid[linha][coluna+j-1]='E'
                    grid[linha][coluna+j-2]='E'
                    grid[linha][coluna+j-3]='E'
            else:
                return False
    
    return True


def posicionar_cruzador(grid, linha, coluna, vertical): #Posiciona o barco cruzador
    global lista_letras
    linha=lista_letras.index(linha)+1
    if vertical==True:
        for i in range(0,3):
            if grid[linha+i][coluna]=="." and (linha+3)<=10:
                if i==2:
                    grid[linha+i][coluna]='C'
                    grid[linha+i-1][coluna]='C'
                    grid[linha+i-2][coluna]='C'
            else: 
                return False
    elif vertical==False:
        for j in range(0,3):
            if grid[linha][coluna+j]=="." and (coluna+3)<=10:
                if j==2:
                    grid[linha][coluna+j]='C'
                    grid[linha][coluna+j-1]='C'
                    grid[linha][coluna+j-2]='C'
            else:
                return False
    return True


def posicionar_submarino(grid, linha, coluna, vertical): #Posiciona o submarino
    global lista_letras
    linha=lista_letras.index(linha)+1
    if vertical==True:
        for i in range(0,2):
            if grid[linha+i][coluna]=="." and (linha+2)<=10:
                if i==1:
                    grid[linha+i][coluna]='S'
                    grid[linha+i-1][coluna]='S'
            else:
                return False
    elif vertical==False:
        for j in range(0,2):
            if grid[linha][coluna+j]=="." and (coluna+2)<=10:
                if j==1:
                    grid[linha][coluna+j]='S'
                    grid[linha][coluna+j-1]='S'
            else:
                return False
    
    return True


def atirar(grid, linha, coluna): # Faz a verificação se a pessoa acertou um alvo ou não.
    simbolo=''
    linha=lista_letras.index(linha)+1
    coluna+=1
    if grid[linha][coluna]=="x" or grid[linha][coluna]=="X":
        print("Você já atirou neste local. Escolha outra coordenada")
        return 0
    elif grid[linha][coluna]==".":
        print("Errou o tiro, acertando apenas água")
        simbolo="x"
    else:
        print("Seu tiro acertou um navio!")
        simbolo="X"
    grid[linha][coluna]=simbolo
    return [linha, coluna, simbolo]

def verificaLetra(ataqueLinha): #Função reposável pro verificar se a letra referente a linha, informada pelo jogador, existe na nossa lista de letras possíveis para as linhas
    for x in range(len(lista_letras)):
        if lista_letras[x]==ataqueLinha:
            return True
    return False
    
def positions(): #Pega as informações de linha e coluna informadas pelo jogador
    global lista_letras
    while True:
        try:
            ataqueLinha=str(input("Insira o valor da linha que deseja atacar: ")).upper()
            ataqueColuna=int(input("Insira o valor da coluna que deseja atacar: "))
            if 0<=ataqueColuna<=10 and verificaLetra(ataqueLinha):
                break
            else:
                print("Valor(es) fora do intervalo adequado!\n")
        except ValueError:
            print("Valor(es) não adequado!\n")
    return ataqueLinha, ataqueColuna


def preparacao(grid): #Prepara um grid posicionando cada um dor barcos.
    global lista_letras
    lista_funcoes=[posicionar_porta_avioes, posicionar_encouracado, posicionar_cruzador, posicionar_submarino]
    for k in range(len(lista_funcoes)):
        temp=False
        while temp==False:
            linha=random.choice(lista_letras)
            coluna=random.randint(1,10)
            vertical=random.choice([False, True])
            temp=lista_funcoes[k](grid,linha,coluna,vertical)
    print("--------------------------------------------------")
    return grid


def menu(): # Cria um menu para jogar novamente ou parar o jogo
    print("\nBATALHA NAVAL")
    print("Menu de opções:")
    print("[1] Iniciar uma nova partida")
    print("[2] Desligar o jogo")
    while True:
        try:
            resposta=int(input())
            if resposta==2:
                return False
            elif resposta==1:
                return True
            else:
                print("Insira um comando válido")
        except ValueError:
            print("Insira um comando válido")
        


def main(): #Realiza a lógica geral
    while menu():
        munição=20
        grid_back=inicializarGrid() # Grid que irá guardar a posições dos barcos
        grid_front=inicializarGrid() # Grid que será mostrada para o jogador
        print("-"*15)
        print("Você tem 20 munições. Boa sorte!")
        preparacao(grid_back)
        #imprimir(grid_back)
        vitoria=False
        abates=14
        while munição!=0:
            imprimir(grid_front)
            ataquelinha,ataqueColuna= positions()
            status=atirar(grid_back,ataquelinha,ataqueColuna)
            if status!=0:
                grid_front[status[0]][status[1]]=status[2] #alteramos a grid que o jogador vê, inserindo X ou x.
                if status[2]=="X":
                    abates-=1
                if abates==0:# Avaliação se o jogador ganhou 
                    vitoria=True
                    break
                munição-=1
            print(f'Munição atual: {munição}')
        imprimir(grid_front)
        if vitoria==True:
            print("\nParabéns, você ganhou!")
        else:
            print("\nQue pena, você perdeu!")
        imprimir(grid_back)


main()