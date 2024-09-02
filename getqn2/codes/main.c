#include <stdio.h>
#include <math.h>


int main(void)
{
	FILE *ptr; //declaring a pointer
	ptr=fopen("main.txt", "w"); // creatnig a mew file to write into
	float mp(float, float) ;
	float f1(float, float) ;
	float f2(float, float) ;

	float x, y;
	x = (float) mp(-5,-4);
	y = (float) mp(7,5);
	fprintf(ptr, "%f\n", x);
	fprintf(ptr, "%f\n", y);

	float u, v, w;
	float p, q, r ;

	v = (float) f1(-5,7);
	p = (float) f2(-5,7);
        w = (float) f1(-4, 5);
	q = (float) f2(-4, 5);
	u = (float) f1(-3,3);
	r = (float) f2(-3,3);

	fprintf(ptr, "%f\n", v);
	fprintf(ptr, "%f\n", p);
	fprintf(ptr, "%f\n", w);
	fprintf(ptr, "%f\n", q);
	fprintf(ptr, "%f\n", u);
        fprintf(ptr, "%f\n", r);

	return 0;
}
