import sys, pygame
import time
from pygame.draw import rect
import random

troca=0
compara=0
screen=pygame.display.set_mode([900,900])

def vetoraleatorio(x):
    vetor=[0]*x
    for i in range(0,len(vetor)):
        vetor[i]=random.randint(1,50)
    return vetor

def partition(lista, inicio, fim):
    global compara, troca, screen
    pivot=lista[fim]
    i=inicio
    eixoX=30
    for j in range(inicio, fim):
        pygame.event.pump()
        screen.fill([0,0,0])
        txt=(f"QuickSort  ||  Comparações={compara}  ||  Trocas={troca}")
        pygame.font.init()
        fonte=pygame.font.get_default_font()
        fontesys=pygame.font.SysFont(fonte, 30)
        txttela = fontesys.render(txt, 1, (255,255,255))
        screen.blit(txttela,(50,50))
        eixoX=30
        for n in range(len(lista)):
            if n==i:
                pygame.draw.rect(screen,[0,0,255],(eixoX,900-lista[n]*16,18,lista[n]*16), width=0)
                eixoX+=20
            elif n==j:
                pygame.draw.rect(screen,[255,255,0],(eixoX,900-lista[n]*16,18,lista[n]*16), width=0)
                eixoX+=20
            elif n==fim:
                pygame.draw.rect(screen,[255,0,0],(eixoX,900-lista[n]*16,18,lista[n]*16), width=0)
                eixoX+=20
            else:
                pygame.draw.rect(screen,[255,255,255],(eixoX,900-lista[n]*16,18,lista[n]*16), width=0)
                eixoX+=20
        pygame.display.flip()
        compara+=1
        if lista[j]<=pivot:
            lista[j], lista[i] = lista[i], lista[j]
            i+=1
            troca+=1
            pygame.mixer.init()
            som=pygame.mixer.Sound("ponto.wav")
            som.play()
        time.sleep(0.1)                        #Aumentar ou diminuir a velocidade da animação
    lista[i],lista[fim]= lista[fim], lista[i]
    return i

def quickSort(lista, inicio, fim):
    if inicio< fim:
        pivot=partition(lista, inicio, fim)
        quickSort(lista, inicio, pivot-1)
        quickSort(lista, pivot+1, fim)
    return lista

def quickFinal(lista):
    global screen
    time.sleep(0.3)
    screen.fill([0,0,0])
    eixoX=30
    for n in range(len(lista)):
        pygame.draw.rect(screen,[255,255,255],(eixoX,900-lista[n]*16,18,lista[n]*16), width=0)
        eixoX+=20
    txt=(f"QuickSort  ||  Comparações={compara}  ||  Trocas={troca}")
    pygame.font.init()
    fonte=pygame.font.get_default_font()
    fontesys=pygame.font.SysFont(fonte, 30)
    txttela = fontesys.render(txt, 1, (255,255,255))
    screen.blit(txttela,(50,50))
    eixoX=30
    pygame.mixer.init()
    som=pygame.mixer.Sound("mixkit-repeating-arcade-beep-1084.wav")
    som.play()
    for a in range(len(lista)):
        pygame.draw.rect(screen,[0,255,0],(eixoX,900-lista[a]*16,18,lista[a]*16), width=0)
        eixoX+=20
        pygame.display.flip()
        time.sleep(0.0605)
    time.sleep(0.30)
    som=pygame.mixer.Sound("mixkit-video-game-win-2016.wav")
    som.play()
    time.sleep(3)