#include <stdio.h>

int main(){
    int T;
    scanf("%d", &T);
    
    int A, B;
    char buffer[20000000];
    int index = 0;
    
    while (T--){
        scanf("%d %d", &A, &B);
        index += sprintf(buffer + index, "%d\n", A+B);
    }
    printf("%s", buffer);
    return 0;
}