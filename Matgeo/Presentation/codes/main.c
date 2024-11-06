#include <stdio.h>
#include <math.h>

int main(void)
{
	FILE *ptr; 
	ptr=fopen("main.txt", "w");
	float mp(float, float) ;
	float norm(float, float, float, float) ;

	float midp1, midp2, dist ;
	midp1 = (float) mp(10,22);
	midp2 = (float) mp(-6,4);
	dist = (float) norm(10,-6,22,4);
        fprintf(ptr, "%f\n", midp1 );
	fprintf(ptr, "%f\n", midp2 );
	fprintf(ptr, "%f", dist );

	return 0;
}

