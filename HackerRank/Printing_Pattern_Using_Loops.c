#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    int n;
    scanf("%d", &n);
    int num = n ;

    int arr  [(( 2 * n )-1) / 2 ] ;

    
    for (int i=0 ; i < (( 2 * n )-1) / 2  ;i++)
    {
        int temp = 0 ;
       
            
        for (int j = 0 ; j <= (( 2 * n )-1) / 2 ; j++ )
        {
            if(j == 0) 
            {
                 printf("%d",num);
                 arr[j] = num ;

                 if( i != 0) temp ++ ;
            }

            else 
            {

                printf(" %d",num-temp) ;
                arr[j] = num-temp ;

                if(temp < i ) temp ++ ;

            }

        }

        for (int k = ( (( 2 * n )-1) / 2 ) - 1 ; k >= 0 ; k-- )
        {
            printf(" %d",arr[k]);

        }

        printf("\n");
    }

    for (int i=(( 2 * n )-1) / 2 ; i >=  0 ; i--)
    {
        int temp = 0 ;

        for (int j = 0 ; j <= (( 2 * n )-1) / 2 ; j++ )
        {
            if(j == 0) 
            {
                 printf("%d",num);
                 arr[j] = num ;

                 if( i != 0) temp ++ ;
            }

            else 
            {

                printf(" %d",num-temp) ;
                arr[j] = num-temp ;

                if(temp < i ) temp ++ ;

            }

        }

        for (int k = ( (( 2 * n )-1) / 2 ) - 1 ; k >= 0 ; k-- )
        {
            printf(" %d",arr[k]);

        }

        printf("\n");
    }
   
        
           
    
    return 0;
}