'''(QUESTÃO 02) Uma empresa de cosméticos comercializa cinco diferentes tipos de produtos e os armazena em
uma estante de 40 x 40 posições. Em cada posição da estante pode ficar apenas uma caixa com um desses
produtos. Para facilitar a identificação, as caixas foram codificadas (etiquetadas) da seguinte forma:
1. Xampu
2. Condicionador
3. Hidratante
4. Tintura
5. Demaquilante
0. Vazio
Nessa situação e considerando um sistema para gerenciar a organização dos produtos na estante, estabeleceuse a declaração de variáveis a seguir:
Com base nesta declaração e considerando a consideração de produtos exposta, faça o que se pede nos itens a
seguir apresentando as soluções em
a) Escreva uma função para ler os códigos dos produtos e armazená-los na matriz Estante.
b) Escreva uma função para contar e imprimir a quantidade de caixas de cada tio de produto na estante.'''
import random
def armazena(estante, produtos):
    for i in range(len(estante)):
        for j in range(len(estante[0])):
            estante[i][j]=produtos[random.randint(0,len(produtos))]
            


def main():
    estante=[0]*40
    for x in range(len(estante)):
        estante[x]=[0]*40
    produtos=["vazio","xampu", "condicionador", "hidratante", "tintura", "demaquilante"]
    contador=[0]*6
    for x in range(len(contador)):
        contador[x]=[0]*6
    armazena(estante, produtos)
    print(estante)

main()