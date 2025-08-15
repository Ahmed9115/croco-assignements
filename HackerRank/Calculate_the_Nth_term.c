#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.

int find_nth_term(int n, int a, int b, int c) {

if (n ==1 )  return a ;
else if (n ==2 ) return b;
else if (n ==3 ) return c;

int count = 4 ;

while (1)
{
int after = a + b + c ;

a = b ;
b = c ;
c = after ;

if (count == n) {return after ; break ;}
count ++ ;
}



}

int main() {
    int n, a, b, c;
  
    scanf("%d %d %d %d", &n, &a, &b, &c);
    int ans = find_nth_term(n, a, b, c);
 
    printf("%d", ans); 
    return 0;
}