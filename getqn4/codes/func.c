#include <math.h>

float mod( float point1[3], float point2[3], float point3[3]) 
{
	return sqrt(pow(point1[0]+point2[0]+point3[0], 2) + pow(point1[1]+point2[1]+point3[1], 2) + pow(point1[2]+point2[2]+point3[2], 2)) ;
}
