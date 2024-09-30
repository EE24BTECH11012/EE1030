#include <stdio.h>
#include <math.h>

double area(double a, double point1[2], double point2[2])
{
	return 2*a*(point2[1]*point2[1] - point1[1]*point1[1]) ;
}

