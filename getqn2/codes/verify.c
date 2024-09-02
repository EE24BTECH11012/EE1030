#include <stdio.h>
#include <math.h>

int main(void)
{
	int size ;
	int matrix[size][size] ;

matrix[0][0] = 1 ;
matrix[0][1] = 1 ;
matrix[0][2] = 1 ;
matrix[1][0] = -5 ;
matrix[1][1] = -4 ;
matrix[1][2] = 0 ;
matrix[2][0] = 7 ;
matrix[2][1] = 5 ;
matrix[2][2] = -3 ;

for (int i=0; i<size; i++)
{
	for (int j=0; j<size; j++)
	{
		printf("%d", matrix[i][j]);
	}
}
int det ;

det = matrix[0][0]*(matrix[1][1]*matrix[2][2] - matrix[2][1]*matrix[1][2]) - matrix[0][1]*(matrix[1][0]*matrix[2][2] - matrix[2][0]*matrix[1][2]) + matrix[0][2]*(matrix[1][0]*matrix[2][1] - matrix[2][0]*matrix[1][1]) ;

printf("The determinant of the given matrix is %d\n", det) ;

matrix[0][0] = 1 ;
matrix[0][1] = 1 ;
matrix[0][2] = 1 ;
matrix[1][0] = -5 ;
matrix[1][1] = 1 ;
matrix[1][2] = 2 ;
matrix[2][0] = 7 ;
matrix[2][1] = -5 ;
matrix[2][2] = -7 ;

printf("The determinant of the given matrix is %d\n", det );

if (det == 0)
{
	printf("The points are collinear.\n");
}
else
{
	printf("The points are not collinear.\n");
}
return 0;
}
