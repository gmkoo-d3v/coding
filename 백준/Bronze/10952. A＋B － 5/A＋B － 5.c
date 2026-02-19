#include <stdio.h>

int main(void) {
    int A, B;
    
    while (scanf("%d %d", &A, &B) ==2) {
        if (A == 0 && B ==0){
            break;
        } else {
            printf("%d\n", A + B);
        }
    }
    return 0;
}