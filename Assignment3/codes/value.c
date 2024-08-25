#include <stdio.h>
#include <math.h>
//includes the contents from Standard Library and Math Library.
int main(void) {
	double M_x, M_y, A_x, A_y, B_x, B_y ;
	M_x = 0 ; M_y = 4 ; A_x = -2 ; A_y = 3 ;
B_x = 2 * M_x - A_x ;
B_y = 2 * M_y - A_y ;
printf("%lf %lf", B_x, B_y);

FILE *fp = fopen( "Value.dat", "w" );
if (fp != NULL)
{
	fprintf(fp, "0,4 -2,3 2,5");
fclose(fp);
}
return 0;
}
