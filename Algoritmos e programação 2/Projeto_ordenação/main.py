'''
Entrega do Trabalho ___- Algoritmos e Programação II
Nós,
Luiz Octavio Tassinari Saraiva
Fabio Domingues Pereira Sabino
declaramos que
todas as respostas são fruto de nosso próprio trabalho,
não copiamos respostas de colegas externos à equipe,
não disponibilizamos nossas respostas para colegas externos ao grupo e
não realizamos quaisquer outras atividades desonestas para nos beneficiar
ou prejudicar outros.
'''

import sys, pygame
import random
from pygame.draw import rect
from BubbleSort import bubblesort
from InsertionSort import insertionsort
from MergeSort import mergeSort, Merge, mergeFinal
from quickSort import quickSort, partition, quickFinal
from SelectionSort import selectionsort

def vetoraleatorio(x):
    vetor=[0]*x
    for i in range(0,len(vetor)):
        vetor[i]=random.randint(1,50)
    return vetor

def main():
    pygame.init()
    bubblesort(vetoraleatorio(30)) #Feito
    selectionsort(vetoraleatorio(30)) #Feito
    insertionsort(vetoraleatorio(30)) #Feito
    mergeFinal(mergeSort(vetoraleatorio(30), 0,30)) #Feito
    quickFinal(quickSort(vetoraleatorio(30), 0,29)) #Feito
    pygame.quit()
main()