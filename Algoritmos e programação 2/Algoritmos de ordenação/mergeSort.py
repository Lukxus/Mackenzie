import random

def Merge(lista, inicio, meio,fim):
    esquerda=lista[inicio:meio]
    direita=lista[meio:fim]
    top_e, top_d=0,0
    for k in range(inicio, fim):
        if top_e>=len(esquerda):
            lista[k]=direita[top_d]
            top_d+=1
        elif top_d>=len(direita):
            lista[k]= esquerda[top_e]
            top_e+=1
        elif esquerda[top_e]<direita[top_d]:
            lista[k]=esquerda[top_e]
            top_e+=1
        else:
            lista[k]=direita[top_d]
            top_d+=1

def mergeSort(lista, inicio, fim):
    if (fim-inicio) > 1:
        meio=(inicio+fim)//2
        mergeSort(lista, inicio, meio)
        print(lista)
        mergeSort(lista, meio, fim)
        print(lista)
        Merge(lista, inicio, meio, fim)
        print(lista)
    return lista

def vetoraleatorio(x):
    vetor=[0]*x
    for i in range(0,len(vetor)):
        vetor[i]=random.randint(1,50)
    return vetor

def vetorOrdenadoCrescente(x):
    vetor=[0]*x
    vetor[0]=random.randint(1,3)
    for linhas in range(1,len(vetor)):
        vetor[linhas]=random.randint(vetor[linhas-1],vetor[linhas-1]+1)
    return vetor

def vetorOrdenadoDecrescente(x):
    vetor=[0]*x
    vetor[0]=random.randint(10,50)
    for linhas in range(1,len(vetor)):
        vetor[linhas]=random.randint(vetor[linhas-1]-5, vetor[linhas-1]-1)
    return vetor
'''
vetor_oito_descrescente=vetorOrdenadoDecrescente(8)
vetor_quinze_descrescente=vetorOrdenadoDecrescente(15)
vetor_oito_crescente=vetorOrdenadoDecrescente(8)
vetor_quinze_crescente=vetorOrdenadoDecrescente(15)
vetor_oito_aleatorio=vetorOrdenadoDecrescente(8)
'''
vetor_oito_aleatorio=vetorOrdenadoDecrescente(8)
vetor_quinze_aleatorio=vetorOrdenadoDecrescente(15)
'''
print("---------------------------------------")
print(vetor_oito_descrescente)
print(mergeSort(vetor_oito_descrescente,0,len(vetor_oito_descrescente)))
print("---------------------------------------")
print(vetor_quinze_descrescente)
print(mergeSort(vetor_quinze_descrescente,0,len(vetor_quinze_descrescente)))
print("---------------------------------------")
print(vetor_oito_crescente)
print(mergeSort(vetor_oito_crescente,0,len(vetor_oito_crescente)))
print("---------------------------------------")
print(vetor_quinze_crescente)
print(mergeSort(vetor_quinze_crescente,0,len(vetor_quinze_crescente)))
print("---------------------------------------")
'''
print(vetor_oito_aleatorio)
print(mergeSort(vetor_oito_aleatorio,0,len(vetor_oito_aleatorio)))
print("---------------------------------------")

'''
print(vetor_quinze_aleatorio)
print(mergeSort(vetor_quinze_aleatorio,0,len(vetor_quinze_aleatorio)))
print("---------------------------------------")

print("TESTE AULA")
vetor=[1,4,8,3,6,5,2,7]
print(vetor)
print(mergeSort(vetor,0,len(vetor)))
'''
