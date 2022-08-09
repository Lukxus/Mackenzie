import random

#busca binária
def buscaBinaria(x,vet):
    low = 0
    high = len(vet)-1

    while low <= high:
        mid = (low+high)//2

        if x == vet[mid]:
            return mid

        if x > vet[mid]:
            low = mid+1
        else:
            high = mid-1
    return -1

#return a primeira ocorrência do elemento x
def buscaPrimeiro(x, vet):
    for i in range(len(vet)):
        if x == vet[i]:
            return i
    return -1

#return a última ocorrência do elemento x
def buscaUltimo(x, vet):
    posicao = -1
    for i in range(len(vet)):
        if x == vet[i]:
            posicao = i
    return posicao

#popular o vetor com numeros aleatorios
def popularVetor(vet):
    n = len(vet)
    for i in range(n):
        vet[i] = random.randint(1,10)
    return vet

def main():
    v=[0]*10

    vet=popularVetor(v)
    print(vet)

    x = int(input("Digite o elemento a ser buscado: "))

    #elemento = buscaPrimeiro(x, vet)
    elemento = buscaUltimo(x, vet)

    if elemento == -1:
        print("Elemento não encontrado no vetor")
    else: print("Elemento encontrado na posição ", elemento, " no vetor")
        
    

main()
    
