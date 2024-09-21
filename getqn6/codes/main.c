#include <stdio.h>
#include <math.h>

float dir(float m, float c) ;
float norm(float m, float c) ;

int main()
{
	FILE *ptr ;
	ptr = fopen("main.txt","w") ;
	
	float m=-1, c=2 ;
	fprintf(ptr, "The direction vector of the given line is %d, %f\n",1,dir(m,c)) ;
	fprintf(ptr, "The normal vector of the given line is %f, %d\n",norm(m,c),1) ;

	return 0 ;
}
	
