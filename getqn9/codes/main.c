#include <stdio.h>
#include <math.h>
#include "func.c"

int main()
{
	int a = 1 ;
	double point1[2] = {2.82,2} ;
	double point2[2] = {4,4} ;

	FILE *ptr ;
	ptr = fopen("main.txt", "w") ;
	for ( float t=0; t<=10; t+=0.5 )
	{
		double x = a*t*2 ;
		double y = a*t*t ;
		fprintf(ptr, "%.2lf %lf\n", x, y) ;
	}
	fprintf(ptr, "%.2lf\n", area(point1[1], point2[1])) ;
	fclose(ptr) ;
	return 0;
}
