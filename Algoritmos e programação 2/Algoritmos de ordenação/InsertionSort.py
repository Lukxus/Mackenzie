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

def insertionSort(vetor):
    inicio=time.time()
    trocas=0
    compara=0
    for i in range(1, len(vetor)):
        x=vetor[i]
        j=i-1
        compara+=1
        while j>=0 and x<vetor[j]:
            vetor[j+1]=vetor[j]
            j-=1 #Faz isso para alguma hora quebrar o loop
            trocas+=1
        vetor[j+1]=x
    print(f"Ocorreram {trocas} trocas")
    print(f"Ocorreram {compara} comparações")
    fim=time.time()
    print(f"Tempo decorrido : {fim-inicio}")
    return vetor
'''
print("---------------------------------------")
insertionSort(vetorOrdenadoDecrescente(100))
print("---------------------------------------")
insertionSort(vetorOrdenadoDecrescente(1000))
print("---------------------------------------")
insertionSort(vetorOrdenadoDecrescente(10000))

print("---------------------------------------")
insertionSort(vetorOrdenadoCrescente(100))
print("---------------------------------------")
insertionSort(vetorOrdenadoCrescente(1000))
print("---------------------------------------")
insertionSort(vetorOrdenadoCrescente(10000))
'''
print("---------------------------------------")
insertionSort(vetoraleatorio(100))
print("---------------------------------------")
insertionSort(vetoraleatorio(1000))
print("---------------------------------------")
insertionSort(vetoraleatorio(10000))
