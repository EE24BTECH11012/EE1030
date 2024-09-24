#include <stdio.h>

void generateLinePoints(float x1, float y1, float x2, float y2, int numPoints, FILE *ptr) {
    for (int i = 0; i <= numPoints; i++) {
        
        float t = (float)i / (float)numPoints;

        
        float x = x1 + t * (x2 - x1);
        float y = y1 + t * (y2 - y1);

        
        fprintf(ptr, "(%.2f, %.2f)\n", x, y);
    }
}

float dir(float x1, float y1, float x2, float y2)
{
	 return (float)(y2-y1)/(float)(x2-x1) ;
}

float norm(float x1, float y1, float x2, float y2 )
{
	return (float)(x1-x2)/(float)(y2-y1);
}
