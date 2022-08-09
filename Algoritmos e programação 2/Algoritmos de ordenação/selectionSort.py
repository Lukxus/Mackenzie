import time
import random

def vetoraleatorio(x):
    vetor=[0]*x
    for i in range(0,len(vetor)):
        vetor[i]=random.randint(1,500)
    return vetor

def vetorOrdenadoCrescente(x):
    vetor=[0]*x
    vetor[0]=random.randint(1,3)
    for linhas in range(1,len(vetor)):
        vetor[linhas]=random.randint(vetor[linhas-1],vetor[linhas-1]+1)
    return vetor

def vetorOrdenadoDecrescente(x):
    vetor=[0]*x
    vetor[0]=random.randint(1000,1050)
    for linhas in range(1,len(vetor)):
        vetor[linhas]=random.randint(vetor[linhas-1]-5, vetor[linhas-1]-1)
    return vetor

def selectionSort(vetor):
    inicio=time.time()
    troca=0
    compara=0
    for k in range(len(vetor)):
        menor= k
        for i in range(k+1, len(vetor)):
            compara+=1
            if vetor[menor]>vetor[i]:
                menor=i
                troca+=1
        aux=vetor[k]
        vetor[k]=vetor[menor]
        vetor[menor]=aux
    print(f"Ocorreram {troca} trocas")
    print(f"Ocorreram {compara} comparações")
    fim=time.time()
    print(f"Tempo decorrido : {fim-inicio}")
    return vetor
'''
print("---------------------------------------")
selectionSort(vetorOrdenadoDecrescente(100))
print("---------------------------------------")
selectionSort(vetorOrdenadoDecrescente(1000))
print("---------------------------------------")
selectionSort(vetorOrdenadoDecrescente(10000))
'''
print("---------------------------------------")
selectionSort(vetorOrdenadoCrescente(100))
print("---------------------------------------")
selectionSort(vetorOrdenadoCrescente(1000))
print("---------------------------------------")
selectionSort(vetorOrdenadoCrescente(10000))
print("---------------------------------------")
selectionSort(vetoraleatorio(100))
print("---------------------------------------")
selectionSort(vetoraleatorio(1000))
print("---------------------------------------")
selectionSort(vetoraleatorio(10000))


