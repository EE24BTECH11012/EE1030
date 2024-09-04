#include <stdio.h>
int determinant(int matrix1[3][3]) ;
int determinant(int matrix2[3][3]) ;

int main() 
{
    int matrix1[3][3] = {
        {1, 1, 1},
        {-4, -5, -6},
        {5, 7, 9}
    };
    
    int det1 = determinant(matrix1);
    
    printf("Determinant of the matrix is: %d\n", det1);

       int matrix2[3][3] = {
        {1, 1, 1},
        {0, 2, -6},
        {-3, -7, 9}
    };
    
    int det2 = determinant(matrix2);
    
    printf("Determinant of the matrix is: %d\n", det2);

   if ( det1 == 0 && det2 == 0 )
   {
	   printf("The given points are collinear.\n");
   }
    return 0;
}

