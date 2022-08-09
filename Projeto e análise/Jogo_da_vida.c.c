/*
Luiz Octavio Tassinari Saraiva - TIA : 32030411
Rodrigo Singh Gedam - TIA : 32128339
Fabio Domingues Pereira Sabino - TIA: 32154429

1. Uma célula viva com 2 ou 3 vizinhos vivos, permanece viva;
2. Uma célula viva com apenas 1 ou 0 vizinhos vivos, morre (solidão);
3. Uma célula viva com 4 ou mais vizinhos, morre (sufocada);
4. Uma célula morta com exatamente 3 vizinhos vivos, renasce
*/

#include <stdio.h>
#include <stdlib.h>

int lin, col;

void preenche(int **celulas)
{
    for (int i=0; i<lin; i++)
    {
        for (int j=0; j<col; j++)
        {
            celulas[i][j]=0;
        }
    }
}

void linhaTabuleiro()
{
    printf("\n");
    for(int i=0; i<col; i++)
    {
        printf("----");
    }
    printf("\n");
}

int printTabuleiro(int **celulas)
{
    linhaTabuleiro();
    for(int i=0; i<lin; i++)
    {
        printf("|");
        for(int j=0; j<col; j++)
        {
            if(celulas[i][j] == 1)
            {
                printf(" * |");
            }
            else if (celulas[i][j] == 0)
            {
                printf("   |");
            }
        }
    linhaTabuleiro();
    }
}

void verificaVizinhos(int **celulas, int **vizinhos)
{
    int contador = 0;
    for (int i=0 ; i<lin ; ++i)
    {
        for (int j=0 ; j<col ; ++j)
        {
            for (int m=i-1 ; m<=i+1 ; ++m)
            {
                for (int n=j-1 ; n<=j+1 ; ++n)
                {
                    if ((m==i && n==j) || (m<0 || n<0) || (m>=lin || n>=col))
                    {
                        continue;
                    }
                    else if (celulas[m][n] == 1)
                    {
                        ++contador;
                    }
                }
            }
            vizinhos[i][j] = contador;
            contador=0;
        }
    }
}

void geracao(int **celulas, int **vizinhos)
{
    for (int i=0 ; i<lin ; ++i)
    {
        for (int j=0 ; j<col ; ++j)
        {
            // 1. Uma célula viva com 2 ou 3 vizinhos vivos, permanece viva ;
            if (celulas[i][j]==1 && (vizinhos[i][j]==2 || vizinhos[i][j]==3))
                continue;

            // 2. Uma célula viva com apenas 1 ou 0 vizinhos vivos, morre (solidão);
            else if (celulas[i][j]==1 && vizinhos[i][j]<=1)
                celulas[i][j]=0;
            
            // 3. Uma célula viva com 4 ou mais vizinhos, morre (sufocada);
            else if (celulas[i][j]==1 && vizinhos[i][j]>=4)
                celulas[i][j]=0;

            // 4. Uma célula morta com exatamente 3 vizinhos vivos, renasce
            else if (celulas[i][j]==0 && vizinhos[i][j]==3)
                celulas[i][j]=1;
        }
    }
}

int main()
{
    int l, c;
    int continuar = 1;
    int **celulas;
    int **vizinhos;

    printf("\n\n***** INICIANDO O JOGO DA VIDA *****\n\n");

    printf("\nConstruindo a matriz. Digite o numero de linhas: ");
    scanf("%d", &lin);
    printf("\nConstruindo a matriz. Digite o numero de colunas: ");
    scanf("%d", &col);
    printf("\nTamanho da matriz: %dx%d", lin, col);
    celulas= malloc(lin * sizeof (int*)) ;
    celulas[0] = malloc (lin * col * sizeof (int)) ;
    vizinhos= malloc(lin * sizeof (int*)) ;
    vizinhos[0] = malloc (lin * col * sizeof (int)) ;
 
    for (int i=1; i < lin; i++){
        celulas[i] = celulas[0] + i * col ;
        vizinhos[i] = vizinhos[0] + i * col ;
    }
    //int celulas[lin][col];
    //int vizinhos[lin][col];
    preenche(celulas);
    preenche(vizinhos);
    while (1)
    {
        printf("\n\n");
        printTabuleiro(celulas);
        printf("\n\n*****DIGITE -1 PARA SAIR DA OPCAO DE ESCOLHA DE CELULAS VIVAS*****\n\n");
        printf("\nDigite valores entre 0 e %d para as linhas\n", lin-1 );
        printf("\nDigite valores entre 0 e %d para as colunas\n", col-1 );
        printf("\n\nEscolha as celulas vivas (linha): ");
        scanf("%d", &l);
        if (l == -1)
            break;
        printf("\nEscolha as celulas vivas (coluna): ");
        scanf("%d", &c);
        if (celulas[l][c] == 1)
            celulas[l][c] = 0;
        else
            celulas[l][c] = 1;
    }

    printf("\n\n");
    printTabuleiro(celulas);
    while (1)
    {
        printf("\n\nDIGITE 1 PARA CONTINUAR OU 0 PARA PARAR. CONTINUAR? ");
        scanf("%d", &continuar);
        if (continuar==1)
        {
            verificaVizinhos(celulas, vizinhos);
            geracao(celulas, vizinhos);
        
            printf("\n");
            printTabuleiro(celulas);
        }
        else
            break;
    }

    printf("\n\n***** FINALIZANDO O JOGO DA VIDA *****\n\n");
    free (celulas[0]) ;
    free (celulas) ;
    free (vizinhos[0]) ;
    free (vizinhos) ;
}
