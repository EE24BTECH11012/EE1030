#include <stdio.h>
#include <math.h>

float mp(float, float) ;

int main(void)
{
	float x, y;
	x = (float) mp(-5,-4);
	y = (float) mp(7,5);
	printf("%f\n", x);
	printf("%f\n", y);
	if ( 2*x + y + 3 == 0 )
	{
		printf("The relation 2x+y=3 is satisfied.\n");
	}
	return 0;
}
