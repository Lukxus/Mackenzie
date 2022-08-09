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

def bubblesort(vetor):
    inicio=time.time()
    trocas=0
    compara=0
    for k in range(len(vetor)):
        for i in range(len(vetor)-1-k):
            compara+=1
            if vetor[i]>vetor[i+1]:
                temp=vetor[i]
                vetor[i]=vetor[i+1]
                vetor[i+1]= temp
                trocas+=1
    print(f"Ocorreram {trocas} trocas")
    print(f"Ocorreram {compara} comparações")
    fim=time.time()
    print(f"Tempo decorrido : {fim-inicio}")
    
    return vetor

print("---------------------------------------")
bubblesort(vetorOrdenadoDecrescente(100))
print("---------------------------------------")
bubblesort(vetorOrdenadoDecrescente(1000))
print("---------------------------------------")
bubblesort(vetorOrdenadoDecrescente(10000))
print("---------------------------------------")
bubblesort(vetorOrdenadoCrescente(100))
print("---------------------------------------")
bubblesort(vetorOrdenadoCrescente(1000))
print("---------------------------------------")
bubblesort(vetorOrdenadoCrescente(10000))
print("---------------------------------------")
bubblesort(vetoraleatorio(100))
print("---------------------------------------")
bubblesort(vetoraleatorio(1000))
print("---------------------------------------")
bubblesort(vetoraleatorio(10000))
