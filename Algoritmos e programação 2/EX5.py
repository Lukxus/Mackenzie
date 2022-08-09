"""
Luiz Octavio Tassinari Saraiva
TIA:32030411
"""
import random

def vetor():
    vetor=[0]*9
    vetor[0]=random.randint(1,2)
    for linhas in range(1,len(vetor)):
        vetor[linhas]=random.randint(vetor[linhas-1],vetor[linhas-1]+1)
    return vetor

def buscaSequencial(matriz,x):
    pos=[]
    cont=0
    for i in range(len(matriz)):
        if matriz[i]==x:
            cont+=1
            pos.append(i)
    return [pos, cont]

def buscaBinaria(vet,x):    # 1 2 3 4 5 5 5 6 7 8 
    low = 0
    high = len(vet)-1
    res=[]
    while low <= high:
        mid = int((low+high)/2)
        if x == vet[mid]:
            contLateral=1
            res.append(mid)
            while mid-contLateral >= 0:
                if vet[mid-contLateral] == x:
                    res.append(mid-contLateral)
                contLateral += 1
            contLateral=1
            while mid+contLateral <= (len(vet)-1):
                if vet[mid+contLateral] == x:
                    res.append(mid+contLateral)
                contLateral += 1
            return res, len(res)
        if x > vet[mid]:
            low = mid+1
        else:
            high = mid-1
    return [res, len(res)]
vet=vetor()
print(vet)
print(buscaBinaria(vet, 5))
print(buscaSequencial(vet, 5))