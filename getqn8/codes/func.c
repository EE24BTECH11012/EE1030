#include <stdio.h>
#include <math.h>

double Area(int n, double centre[n], double otherPoint[n])
{
	double radius, value=0 ;
	for ( int i=0; i<n; i++)
	{
		value += pow(centre[i] - otherPoint[i], 2) ;
	}
	radius = (double)sqrt(value) ;
	double area = 3.14159 * radius * radius ;
	return area ;
}
