#include <stdio.h>
#include <math.h>
#include "func.c"
int main()
{
	FILE *ptr ;
	ptr=fopen("main.txt", "w") ;
	

	float point1[3] = { 2, 3, -4 } ;
	float point2[3] = { 3, -4, -5 } ;
	float point3[3] = { 3, 2, -3} ;

	float modulus = mod(point1, point2, point3) ;
	fprintf(ptr, "%f\n", modulus) ;

	return 0;
}
