#include <stdio.h>

int main(void) {
    int flag = 0;
    int count = 0;
    char sentence[1000002];
    gets(sentence);
    
    for (int i = 0; i <strlen(sentence); i++){
        if (sentence[i] != 32) {
            if (flag == 0) {
                flag = 1;
                count += 1;                
            }            
        }
        else
            flag = 0;
    }
    printf("%d", count);
    return 0;
}