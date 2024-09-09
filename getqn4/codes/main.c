#include <stdio.h>
#include <math.h>

int main()
{
	FILE *ptr ;
	ptr=fopen("main.txt", "w") ;
	float mod(float, float, float, float, float, float, float, float, float) ;

	float a=2; float b=3;float c=-4;float d=3;float e=-4;float f=-5;float g=3; float h=3;float i=-3 ;
	float modulus = (float) mod(a,b,c,d,e,f,g,h,i) ;
	fprintf(ptr, "%f", modulus) ;
	return 0;
}
