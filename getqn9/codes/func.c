#include <stdio.h>
#include <math.h>

double function(double x, double a)
{
	return 4*a*x ;
}

double area(double lower_limit, double upper_limit)
{
	double sum=0 ;
	double function(double, double) ;
	for ( double i = lower_limit; i<=upper_limit; i+=0.01 )
	{
		sum += function(i+0.50, 1) ;
	}
	return sum ;
}


