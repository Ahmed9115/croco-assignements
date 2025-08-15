#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

int number ;
scanf("%d",&number);
int sum = 0;


for(int i =0 ; i < number; i++)
{
int num ;
scanf("%d",&num);
sum += num ;


}

printf("%d",sum);

    return 0;
}
