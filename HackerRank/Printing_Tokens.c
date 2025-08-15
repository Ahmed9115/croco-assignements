#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    char *s;
    s = malloc(1024 * sizeof(char));
    scanf("%[^\n]", s);
    s = realloc(s, strlen(s) + 1);
    int count = 0;

    while(1) {
        if(s[count] == '\0') break;
        if(s[count] == ' ') printf("\n");
        else printf("%c", s[count]);
        count++;
    }

    free(s); 
    return 0;
}