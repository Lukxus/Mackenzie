'''
(QUESTÃO 01) Uma empresa trabalha na produção de concreto e terceiriza o serviço de transporte de produtos.
Os caminhoneiros telefonam para a empresa e registram seu interesse pelo trabalho. Todas as manhãs os
caminhoneiros estacionam o caminhão no pátio da empresa e aguardam sua vez. O atendimento segue o critério
de ordem de chegada. Esse processo é atualmente controlado pela secretária que utiliza sua agenda para
gerenciar os motoristas diariamente. A empresa que carrega no máximo 10 caminhões por dia pretende
informatizar esse processo.
Para a solução do problema apresenta-se a seguir um pseudocódigo que utiliza o conceito de fila, mantendo os
elementos sempre nas primeiras posições do vetor:

Com base nas informações apresentadas, faça o que se pede nos itens a seguir:
a) Implemente a função desenfileirar() que deve remover e retornar um elemento representado por um
caminhoneiro da fila ou a mensagem “Fila Vazia” se não houver elementos.
b) Implemente o procedimento mostrarFila() que deve apresentar a fila de elementos, ou seja, os
caminhoneiros que estão na fila.
'''
def estaVazia(total):
    if total==0:
        return True
    else:
        return False

def estaCheia(total):
    if total>=10:
        return True
    else:
        return False

def desenfileirar(vetor):
    for x in range(len(vetor)-1,-1,-1):
        if vetor[x]!="":
            aux=vetor[x]
            vetor[x]=""
            return aux
        if x==0 and vetor[x]=="":
            print("Vetor vazio!")

def mostraFila(vetor):
    for i in range(len(vetor)):
        print(vetor[i])
def main():
    caminhoneiros=['']*10
    total=0
    while True:
        escolha=int(input("Digite 1 para enfileirar ou 2 para desenfileirar: "))
        if escolha==1:
            if (estaCheia(total)==False):
                caminhoneiro=input("Digite o nome do caminhoneiro: ")
                caminhoneiros[total]=caminhoneiro
                total=total+1
            else:
                print("Fila cheia")
                break
        else:
            retirado=desenfileirar(caminhoneiros)
            print(f"Retirado:{retirado}")
        mostraFila(caminhoneiros)
main()