#include <stdio.h>

int main(void) {
    int N, X;
    scanf("%d %d", &N, &X);
    
    int Start = 1;
    
    for (int i = 0; i < N ; i++) {
        int a;
        scanf("%d", &a);
        if (a < X) {
            if (!Start) {
                printf(" ");
            }
            printf("%d", a);
            Start = 0;
        }
    }
    printf("\n");
    return 0;
}