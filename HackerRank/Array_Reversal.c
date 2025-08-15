#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

int number ;
scanf("%d",&number);
int arr[number];


for(int i =0 ; i < number; i++)
{
int num ;
scanf("%d ",&num);
arr[i] = num ;


}
for(int i =number - 1 ; i >= 0; i--)
{
printf("%d ",arr[i]);
}


    return 0;
}