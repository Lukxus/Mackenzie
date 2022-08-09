from function import sequencia
import random

def iniciarJogo():
    while True:
        try:
            N=int(input("Informe o tamanho da sequência do jogo: "))
            if N==-1:
                break
            elif N<-1 or N==0:
                print("Digite um valor válido.")
            else:
                sequencia(N)
        except TypeError:
            print("Digite um valor válido.")
        except ValueError:
            print("Digite um valor válido.")

def entrada():
    listaJogos=[]
    arquivo_partida=open('registro.txt', 'r')
    while True:
        partidas=arquivo_partida.readline().rstrip()
        if partidas=='':
            break
        intermed=partidas.split(' ')
        for i in range(len(intermed)):
            intermed[i]=int(intermed[i])
        listaJogos.append(intermed)
    return listaJogos

def vez(lista, indice):
    while True:
        try:
            jogador_escolha=int(input(f'\n{lista[indice%2]} Escolha entre par[0] ou ímpar[1]: '))
            if jogador_escolha==1 or jogador_escolha==0:
                break
            else:
                print("Digite um valor entre 0 e 1.")
        except TypeError:
            print("Digite um valor válido.")
        except ValueError:
            print("Digite um valor válido.")
    par_impar=random.randint(1,10)
    if par_impar%2==jogador_escolha:
        return [lista[0],lista[1]]
    else:
        return [lista[1], lista[0]]

def saida(lista_vencedor):
    arquivo_vencedor=open('registro_vencedor.txt', 'a+')
    for i in range(len(lista_vencedor)):
        arquivo_vencedor.write(lista_vencedor[i]+'\n')
    arquivo_vencedor.close()

def bubbleSort(Vetor, listaNomes):
    contador=0
    print(listaNomes)
    for k in range(len(Vetor)):
        for i in range(len(Vetor)-1-k):
            if Vetor[i]> Vetor[i+1]:
                temp=Vetor[i]
                Vetor[i]=Vetor[i+1]
                Vetor[i+1]=temp
                print(listaNomes[contador%2])
                print(Vetor)
                contador+=1    
    if contador>=1:    
        return [Vetor, listaNomes[(contador%2)-1]]
    else:
        return [Vetor, listaNomes[(contador%2)]]
    

def main():
    arquivo=open("registro.txt","w")
    arquivo.write("")
    arquivo.close()
    lista_vencedor=[]
    nome1=str(input('Digite o nome do jogador 1: '))
    nome2=str(input('Digite o nome do jogador 2: '))
    iniciarJogo()
    lista_jogos=entrada()
    for partida in range(len(lista_jogos)):
        print(f"\n{partida+1}° Partida")
        print(lista_jogos[partida])
        lista_nomes=vez([nome1,nome2],partida)
        print(f"{lista_nomes[0]} começa!")
        Resposta=bubbleSort(lista_jogos[partida], lista_nomes)
        print(Resposta[0])
        print(f"{Resposta[1]} Ganhou!")
        lista_vencedor.append(Resposta[1])
    saida(lista_vencedor)

main()
