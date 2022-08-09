#include <stdio.h>
/*
Biblioteca padrão de entrada e saida de dados.
*/
#include <string.h>
/*
Copiar strings em C usando strcpy e strncpy;
Concatenar strings em linguagem C usando strcat e strncat;
Descobrir o tamanho de uma string em C usando strlen();
Comparar strings em C usando strcmp();
*/
#include <conio.h>
/*
É para desenhar tela, e é para dos/windows (as funções do conio 
são úteis para manipular caracteres na tela, especificar cor de carácter e de fundo.)
*/
 
int main(){
    int a=3;
    int b=5;
    int *p1; //ponteiero
    int z;
    int v[10];
    int f[10];
    char palavra[10];
    char termo="termo";

    /*
    Em C e em C ++, aspas simples identificam um único caractere, enquanto aspas duplas criam uma string literal. 
    'a' é um literal de um caractere único, enquanto "a" é um literal de cadeia de caracteres que contém um 'a' 
    terminador e um nulo (que é uma matriz de 2 caracteres).
    */
    printf("Tamanho da palavra 'termo' : %d",strlen("termo"));
    //printf("*char' : %d",);
    printf("\nDigite uma palavra:");
    scanf("\n%s", &palavra);
    printf("%s\n",palavra);
    
    //VETORES
    //preenchendo os vetores;
    for (int i=0; i<10;i++){
        if (i<=9){
            v[i]=i+2;
            f[i]=i+3;
        }
    }
    
    for (int q=0; q<=9;q++){
        printf("\nv[%d] : %d\n",q,v[q]);
        printf("\nf[%d] : %d\n",q,f[q]);
    }
    //Vetores fim.
    printf("\na=%d, b=%d, p1=%d, z=%d\n\n", a,b,p1,z);
    p1=&a; //assim atribuimos ao ponteiro, o valor do endereço do a ; 
    printf("\na=%d, b=%d, p1=%d, z=%d\n\n", a,b,p1,z);
    *p1=10; // Assim mudamos o conteudo que aponta o ponteiro
    printf("\na=%d, b=%d, p1=%d, z=%d\n\n", a,b,p1,z);
    z=*p1;
    printf("\na=%d, b=%d, p1=%d, z=%d\n\n", a,b,p1,z);
    *p1=100;
    printf("\na=%d, b=%d, p1=%d, z=%d\n\n", a,b,p1,z);
    
}
   