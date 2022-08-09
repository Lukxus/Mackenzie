import sys, pygame
import time
import random
from pygame.draw import rect

def insertionsort(lista):
    troca=0
    compara=0
    screen=pygame.display.set_mode([900,900])
    for i in range(1, len(lista)):
        pygame.event.pump()
        x=lista[i]
        j=i-1
        while j>=0 and x<lista[j]:
            lista[j+1]=lista[j]
            j-=1 #Faz isso para alguma hora quebrar o loop
            compara+=1
            screen.fill([0,0,0])
            txt=(f"InsertionSort  ||  Comparações={compara}  ||  Trocas={troca}")
            pygame.font.init()
            fonte=pygame.font.get_default_font()
            fontesys=pygame.font.SysFont(fonte, 30)
            txttela = fontesys.render(txt, 1, (255,255,255))
            screen.blit(txttela,(25,25))
            eixoX=30
            for n in range(len(lista)):
                if n==i:
                    pygame.draw.rect(screen,[255,255,0],(eixoX,900-lista[n]*16,18,lista[n]*16), width=0)
                    eixoX+=20
                elif n==j:
                    pygame.draw.rect(screen,[0,0,255],(eixoX,900-lista[n]*16,18,lista[n]*16), width=0)
                    eixoX+=20
                else:
                    pygame.draw.rect(screen,[255,255,255],(eixoX,900-lista[n]*16,18,lista[n]*16), width=0)
                    eixoX+=20
            pygame.display.flip()
            time.sleep(0.2)                        #Aumentar ou diminuir a velocidade da animação
        lista[j+1]=x
        troca+=1
        pygame.mixer.init()
        som=pygame.mixer.Sound("ponto.wav")
        som.play()
    time.sleep(0.05)
    screen.fill([0,0,0])
    eixoX=30
    txt=(f"SelectionSort  ||  Comparações={compara}  ||  Trocas={troca}")
    pygame.font.init()
    fonte=pygame.font.get_default_font()
    fontesys=pygame.font.SysFont(fonte, 30)
    txttela = fontesys.render(txt, 1, (255,255,255))
    screen.blit(txttela,(50,50))
    for n in range(len(lista)):
        pygame.draw.rect(screen,[255,255,255],(eixoX,900-lista[n]*16,18,lista[n]*16), width=0)
        eixoX+=20
    pygame.display.flip()
    time.sleep(0.35)
    pygame.event.pump()
    som=pygame.mixer.Sound("mixkit-repeating-arcade-beep-1084.wav")
    som.play()
    eixoX=30
    for a in range(len(lista)):
        pygame.draw.rect(screen,[0,255,0],(eixoX,900-lista[a]*16,18,lista[a]*16), width=0)
        eixoX+=20
        pygame.display.flip()
        time.sleep(0.0605)
    time.sleep(0.30)
    som=pygame.mixer.Sound("mixkit-video-game-win-2016.wav")
    som.play()
    time.sleep(3)