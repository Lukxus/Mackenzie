import random
def vetorOrdenadoDecrescente(x):
    vetor=[0]*x
    vetor[0]=random.randint(5,15)
    for linhas in range(1,len(vetor)):
        vetor[linhas]=random.randint(vetor[linhas-1]-1, vetor[linhas-1]-1)
    return vetor

def partition(lista, inicio, fim):
    pivot=lista[fim]
    i=inicio
    for j in range(inicio, fim):
        print(lista)
        if lista[j]<=pivot:
            lista[j], lista[i] = lista[i], lista[j]
            i+=1 
    lista[i],lista[fim]= lista[fim], lista[i]
    return i

def quickSort(lista, inicio, fim):
    if inicio< fim:
        pivot=partition(lista, inicio, fim)
        quickSort(lista, inicio, pivot-1)
        quickSort(lista, pivot+1, fim)

listadec= vetorOrdenadoDecrescente(5)
quickSort(listadec, 0, len(listadec)-1)