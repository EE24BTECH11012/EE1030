#include <stdio.h>

void twoDtriangle_gen( double, double, double, char* ) ;
int main()
{
	double sideAB=4, sideBC=6, sideCA=9 ;
	
	twoDtriangle_gen(sideAB, sideBC, sideCA, "triangle.txt") ;

	return 0;
}
