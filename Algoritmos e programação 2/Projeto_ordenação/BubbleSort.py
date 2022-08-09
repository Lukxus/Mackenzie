import sys, pygame
import time
from pygame.draw import rect

def bubblesort(lista):
    trocas=0
    compara=0
    screen=pygame.display.set_mode([900,900])
    eixoX=30
    for k in range(len(lista)):
        for i in range(len(lista)-1-k):
            pygame.event.pump()
            screen.fill([0,0,0])
            txt=(f"BubbleSort  ||  Comparações={compara}  ||  Trocas={trocas}")
            pygame.font.init()
            fonte=pygame.font.get_default_font()
            fontesys=pygame.font.SysFont(fonte, 30)
            txttela = fontesys.render(txt, 1, (255,255,255))
            screen.blit(txttela,(25,25))
            compara+=1
            eixoX=30
            for n in range(len(lista)):
                if n==i:
                    pygame.draw.rect(screen,[0,0,255],(eixoX,900-lista[n]*16,18,lista[n]*16), width=0)
                    eixoX+=20
                elif n==i+1:
                    pygame.draw.rect(screen,[255,255,0],(eixoX,900-lista[n]*16,18,lista[n]*16), width=0)
                    eixoX+=20
                else:
                    pygame.draw.rect(screen,[255,255,255],(eixoX,900-lista[n]*16,18,lista[n]*16), width=0)
                    eixoX+=20
            pygame.display.flip()
            if lista[i]>lista[i+1]:
                temp=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]= temp
                trocas+=1
                pygame.mixer.init()
                som=pygame.mixer.Sound("ponto.wav")
                som.play()
            time.sleep(0.1)                        #Aumentar ou diminuir a velocidade da animação
    eixoX=30
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