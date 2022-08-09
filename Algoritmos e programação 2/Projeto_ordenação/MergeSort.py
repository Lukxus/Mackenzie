import sys, pygame
import time
from pygame import display
from pygame.draw import rect
import random

troca=0
compara=0

def Merge(lista, inicio, meio,fim):
    global compara, troca
    esquerda=lista[inicio:meio]
    direita=lista[meio:fim]
    top_e, top_d=0,0
    screen=pygame.display.set_mode([900,900])
    for k in range(inicio, fim):
        pygame.event.pump()
        eixoX=30
        screen.fill([0,0,0])
        txt=(f"MergeSort  ||  Comparações={compara}  ||  Trocas={troca}")
        pygame.font.init()
        fonte=pygame.font.get_default_font()
        fontesys=pygame.font.SysFont(fonte, 30)
        txttela = fontesys.render(txt, 1, (255,255,255))
        screen.blit(txttela,(50,50))
        for n in range(len(lista)):
            if n==k:
                pygame.draw.rect(screen,[255,0,0],(eixoX,900-lista[n]*16,18,lista[n]*16), width=0)
                eixoX+=20
            elif n==inicio or n==fim or n==meio:
                pygame.draw.rect(screen,[0,0,255],(eixoX,900-lista[n]*16,18,lista[n]*16), width=0)
                eixoX+=20
            else:
                pygame.draw.rect(screen,[255,255,255],(eixoX,900-lista[n]*16,18,lista[n]*16), width=0)
                eixoX+=20
            time.sleep(0.01)                        #Aumentar ou diminuir a velocidade da animação
        pygame.display.flip()
        if top_e>=len(esquerda):
            lista[k]=direita[top_d]
            top_d+=1
            troca+=1
            pygame.mixer.init()
            som=pygame.mixer.Sound("ponto.wav")
            som.play()
        elif top_d>=len(direita):
            lista[k]= esquerda[top_e]
            top_e+=1
            troca+=1
            pygame.mixer.init()
            som=pygame.mixer.Sound("ponto.wav")
            som.play()
        elif esquerda[top_e]<direita[top_d]:
            lista[k]=esquerda[top_e]
            top_e+=1
            troca+=1
            pygame.mixer.init()
            som=pygame.mixer.Sound("ponto.wav")
            som.play()
        else:
            lista[k]=direita[top_d]
            top_d+=1
        compara+=1
    eixoX=30
    screen.fill([0,0,0])
    txt=(f"MergeSort  ||  Comparações={compara}  ||  Trocas={troca}")
    pygame.font.init()
    fonte=pygame.font.get_default_font()
    fontesys=pygame.font.SysFont(fonte, 30)
    txttela = fontesys.render(txt, 1, (255,255,255))
    screen.blit(txttela,(50,50))
    for n in range(len(lista)):
        if n==k:
            pygame.draw.rect(screen,[255,0,0],(eixoX,900-lista[n]*16,18,lista[n]*16), width=0)
            eixoX+=20
        elif  n==inicio or n==fim or n==meio:
            pygame.draw.rect(screen,[0,0,255],(eixoX,900-lista[n]*16,18,lista[n]*16), width=0)
            eixoX+=20
        else:
            pygame.draw.rect(screen,[255,255,255],(eixoX,900-lista[n]*16,18,lista[n]*16), width=0)
            eixoX+=20
        time.sleep(0.01)                        #Aumentar ou diminuir a velocidade da animação
    pygame.display.flip()

def mergeSort(lista, inicio, fim):
    if (fim-inicio) > 1:
        meio=(inicio+fim)//2
        mergeSort(lista, inicio, meio)
        mergeSort(lista, meio, fim)
        Merge(lista, inicio, meio, fim)
    return lista

def mergeFinal(lista):
    screen=pygame.display.set_mode([900,900])
    screen.fill([0,0,0])
    txt=(f"MergeSort  ||  Comparações={compara}  ||  Trocas={troca}")
    pygame.font.init()
    fonte=pygame.font.get_default_font()
    fontesys=pygame.font.SysFont(fonte, 30)
    txttela = fontesys.render(txt, 1, (255,255,255))
    screen.blit(txttela,(50,50))
    eixoX=30
    for n in range(len(lista)):
        pygame.draw.rect(screen,[255,255,255],(eixoX,900-lista[n]*16,18,lista[n]*16), width=0)
        eixoX+=20
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