#include <stdio.h>
#include <math.h>
#include "func.c" 

int main() {
    int n = 2;
    double centre[2] = {1.0, 2.0};
    double otherPoint[2] = {4.0, 6.0};

    FILE *ptr = fopen("main.txt", "w");
    if (ptr == NULL) {
        perror("Error opening the file");
        return 1;
    }
    double k ;
	
	for ( k=-1; k<=1; k+=0.05 )
	{
		double x = centre[0] + 5*k ;
		double y1 = centre[0] + 5*sqrt(1-pow(k,2)) ;
		fprintf(ptr, "%lf,%lf\n", x, y1) ;	
	}
	for ( k=1; k>=-1; k-=0.05 )
	{
		double x = centre[0] + 5*k ;
		double y1 = centre[0] - 5*sqrt(1-pow(k,2)) ;
		fprintf(ptr, "%lf,%lf\n", x, y1) ;	
	}
	fprintf(ptr, "-1,5.60") ;

	
    fprintf(ptr, "%lf\n", area(n, centre, otherPoint));
    fclose(ptr);
    printf("The values have been printed to main.txt\n");

    return 0;
}
