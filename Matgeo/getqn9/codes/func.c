#include <stdio.h>
#include <math.h>

double function(double x, double a)
{
	return 2*sqrt(a*x)  ;
}

double area(double lower_limit, double upper_limit)
{
	double sum=0 ;
	//double function(double, double) ;
	for ( double i = lower_limit; i<=upper_limit; i+=1e-7 )
	{
		sum += function(i, 1)*1e-7 ;
	}
	return sum ;
}

