#include <stdio.h>

int SomaRecurssiva(int x, int y){
    if (x==0){
        return y;
    }
    else if (y==0){
        return x;
    }
    else{
        return SomaRecurssiva(x,y-1)+1;
    }
    
}

int main(){
    
    int res=SomaRecurssiva(0,2);
    printf("%d",res);
}