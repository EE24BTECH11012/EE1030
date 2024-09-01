#include <stdio.h>
#include <math.h>


int main(void)
{
	FILE *ptr; //declaring a pointer
	ptr=fopen("main.txt", "w"); // creatnig a mew file to write into
	float mp(float, float) ;

	float x, y;
	x = (float) mp(-5,-4);
	y = (float) mp(7,5);
	fprintf(ptr, "%f\n", x);
	fprintf(ptr, "%f\n", y); //storing the values in the new file created.
	return 0;
}
