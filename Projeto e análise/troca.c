void troca (int a, int b){
    int aux;
    int *p1=a;
    int *p2=b;
    aux=*p1;
    *p1=*p2;
    *p2=aux;
}

int main(void){
    int x =1, y=2;
    printf("Antes: x=%d e y=%d\n", x,y);
    troca(&x,&y);
    printf("Depois: x=%d e y=%d\n", x,y);
    return 0;
}