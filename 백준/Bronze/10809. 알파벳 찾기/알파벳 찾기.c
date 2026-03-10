#include <stdio.h>

int main(void) {
    char S[101];
    int result[26];

    scanf("%s", S);

    for (int i = 0; i < 26; i++) {
        result[i] = -1;
    }

    for (int i = 0; S[i] != '\0'; i++) {
        int index = S[i] - 'a';

        if (result[index] == -1) {
            result[index] = i;
        }
    }

    for (int i = 0; i < 26; i++) {
        printf("%d ", result[i]);
    }
    return 0;

}
