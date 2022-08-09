'''
Entrega do Trabalho Jogo da Velha - Algoritmos e Programação II
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


def initialize(): #Inicializa a matriz
    return(
    [['-','-','-'],
    ['-','-','-'],
    ['-','-','-']]
    )

def empate(M): #Diz se o jogo chegou ao fim por empate
    fim=True
    for l in range(len(M)):
        for c in range(len(M[0])):
            if M[l][c]=='-':
                fim=False
    return fim

def status(M): #Verifica se alguém ganhou ou se o jogo deve continuar
    if empate(M)==True:
        return 0
    for linhas in range(len(M)): #Verificação das linhas
        if M[linhas][0]==M[linhas][1]==M[linhas][2] :
            if M[linhas][0]=='O':
                return 1
            elif M[linhas][0]=='X':
                return 2
    for colunas in range(len(M[0])): #Verificação das colunas
        if M[0][colunas]==M[1][colunas]==M[2][colunas]:
            if M[0][colunas]=='O':
                return 1
            elif M[0][colunas]=="X" :
                return 2
    if M[0][0]==M[1][1]==M[2][2]: #Diagonal Principal
        if M[0][0]=='O':
            return 1
        elif M[0][0]=='X':
            return 2
    elif M[0][2]==M[1][1]==M[2][0]:  #Diagonal Secundária
        if M[0][2]=='O':
            return 1
        elif M[0][2]=='X':
            return 2
    return -1

def posElemento(M): # faz a leitura e validação de valores validos para inserção dos elementos na matriz
    while True:
            try:
                linha=int(input("Informe a linha do elemento que quer inserir:"))-1
                if linha<= len(M)-1 and linha >= 0:
                    break
                else:
                    print("Valor inválido!")
            except ValueError:
                print("Digite um valor adequado para a posição do elemento.")
    while True:
        try:
            coluna=int(input("Informe a coluna do elemento que quer inserir:"))-1
            if coluna<= len(M[0])-1 and coluna >= 0:
                    break
            else:
                print("Valor inválido!")
        except ValueError:
            print("Digite um valor adequado para a posição do elemento:")
    return [linha, coluna]

#Apesar de não retornar nada, ela altera a própria matriz que lhe foi passada como argumento
def step(M,lin,col, Gamer): #simbolo--> X ou O
    while True:
        if M[lin][col]=="-":
            M[lin][col]= Gamer
            return True
        else:
            return False

def mostraTabuleiro(matriz): #Mostra o tabuleiro
    print()
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if j!=len(matriz[0])-1:
                print(matriz[i][j], end=' | ')
            else:
                print(matriz[i][j])
        if i!=(len(matriz)-1):
            print('---------')


def registro(resultado):  # Grava as informações da partida num arquivo.txt
    registro_write=open("Registro.txt", "a+")
    registro_read=open("Registro.txt", "r")
    partida=1
    while True:
        line=registro_read.readline().rstrip()
        if line=='':
            break
        partida+=1
    registro_write.write(str(partida)+resultado+'\n')
    registro_write.close()
    registro_read.close()


def game(): # Faz a lógica geral do funcionamento do projeto
    print("JOGO DA VELHA")
    print("Os valores válidos para as linhas e colunas são de 1 a 3. Assim, a primeira linha e primeira coluna corresponde ao valor 1x1")
    print("-"*20)
    matriz=initialize()
    mostraTabuleiro(matriz)
    cont=0
    while True:
        change=False
        if cont%2==0: #Vez jogador 1
            print("\nVez do jogador O")
            while change==False:
                position=posElemento(matriz)
                change=step(matriz,position[0],position[1], 'O')
                if change ==True:
                    break
                print('\nValor inválido')
        else: #Vez jogador 2
            print("\nVez do jogador X")
            while change==False:
                position=posElemento(matriz)
                change=step(matriz,position[0],position[1], 'X')
                if change ==True:
                    break
                print('\nValor inválido')
        mostraTabuleiro(matriz)
        if cont>=4: # A partir da 4 rodada, começa a ser feita a verificação a procura de um ganhador ou do fim do jogo/empate
            Situation=status(matriz)
            if Situation == 0:
                print("\nEmpate")
                resultado=("; Empate")
                registro(resultado)
                break
            if Situation == 1:
                print("\nO Venceu")
                resultado=(" ; O")
                registro(resultado)
                break
            if Situation == 2:
                print("\nX Venceu")
                resultado=(" ; X")
                registro(resultado)
                break
        cont+=1
game()