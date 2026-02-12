#include <stdio.h>

int main(void){
    long long X=0;
    long long N=0;
    long long total=0;
    long long a=0;
    long long b=0;

    scanf("%lld", &X);
    scanf("%lld", &N);
    
    for (int i = 0; i <N; i++){
        scanf("%lld %lld", &a,&b);
        total +=a*b;
    }
    
    if (total== X){
        printf("Yes\n");
    } else{
        printf("No\n");
    }
    return 0;

}