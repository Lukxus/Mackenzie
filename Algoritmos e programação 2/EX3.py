"""
Luiz Octavio Tassinari Saraiva
TIA:32030411
"""
import random

def matriz():
    matriz=[0]*10
    for linhas in range(10):
        matriz[linhas]=[0]*10
    for linhas in range(10):
        for colunas in range(10):
            matriz[linhas][colunas]=random.randint(1,20)
    return matriz

def ACP(matriz):
    listaAcima=[]
    for linhas in range(len(matriz)):
        for colunas in range(len(matriz)):
            if colunas> linhas:
                listaAcima.append(matriz[linhas][colunas])
    return listaAcima

def ABP(matriz):
    listaAbaixo=[]
    for linhas in range(len(matriz)):
        for colunas in range(len(matriz)):
            if linhas> colunas:
                listaAbaixo.append(matriz[linhas][colunas])
    return listaAbaixo

def mostra(matriz):
    for linha in range(len(matriz)):
        print(matriz[linha])

def principal(matriz):
    listaPrincipal=[]
    for linhas in range(len(matriz)):
        for colunas in range(len(matriz)):
            if linhas==colunas:
                listaPrincipal.append(matriz[linhas][colunas])
    return listaPrincipal

def secundaria(matriz):
    listaSecundaria=[]
    for linhas in range(len(matriz)):
        for colunas in range(len(matriz)):
            if linhas+colunas==10:
                listaSecundaria.append(matriz[linhas][colunas])
    return listaSecundaria 
x=matriz()
mostra(x)
print(f"\nAcima: {ACP(x)}, Soma={sum(ACP(x))}")
print(f"\nAbaixo: {ABP(x)}, Soma={sum(ABP(x))}")
print(f"\nPrincipal: {principal(x)}, Soma={sum(principal(x))}")
print(f"\nSecundaria: {secundaria(x)}, Soma={sum(secundaria(x))}")