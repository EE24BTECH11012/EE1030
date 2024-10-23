#include <stdio.h>

void generateLinePoints(float x[2], float y[2], int numPoints, FILE *ptr) {
    for (int i = 0; i <= numPoints; i++) {
        
        float t = (float)i / (float)numPoints;

        
        float xcoord = x[0] + t * (x[1] - x[0]);
        float ycoord = y[0] + t * (y[1] - y[0]);

        
        fprintf(ptr, "(%.2f, %.2f)\n", xcoord, ycoord);
    }
}

void dir(float a, float b, float c, float arr[2])
{
	arr[0] = -a/b ;
	arr[1] = (float)1 ;
}
void norm(float a, float b, float c, float arr[2])
{
	arr[0] = (float)1 ;
	arr[1] = a/b ;
}
float dotproduct(int n, float vec1[n], float vec2[n]) 
{
	float ans = 0 ;
	for ( int i=0; i<n; i++ )
	{
		ans += vec1[i]*vec2[i] ;
	}
	return ans ;
}
			
