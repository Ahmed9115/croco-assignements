#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

char *STRING ;
STRING = (char*)malloc(1024 * sizeof(char));
fgets(STRING, 1024 , stdin);
realloc(STRING,strlen(STRING));
int frequency [10] = {0};


for(int i = 0 ; i < strlen(STRING) ; i++)
{
        switch (STRING[i])
        {
            case '0':
            frequency[0]++;
            break;

            case '1':
            frequency[1]++;
            break;

            case '2':
            frequency[2]++;
            break;

            case '3':
            frequency[3]++;
            break;

            case '4':
            frequency[4]++;
            break;

            case '5':
            frequency[5]++;
            break;

            case '6':
            frequency[6]++;
            break;

            case '7':
            frequency[7]++;
            break;

            case '8':
            frequency[8]++;
            break;

            case '9':
            frequency[9]++;
            break;
        }

}

for (int i = 0 ; i <= 9 ; i++)
{printf("%d ",frequency[i]);}

free(STRING);

return 0;
}
