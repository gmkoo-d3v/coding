#include <stdio.h>

int main(void) {
    int T;
    scanf("%d", &T);

    for (int k = 0; k < T; k++) {
        int R;
        char S[21];

        scanf("%d %s", &R, S);

        for (int i = 0; S[i] != '\0'; i++) {
            for (int j = 0; j < R; j++)
                printf("%c", S[i]);
        }
        printf("\n");
    }
    return 0;
}