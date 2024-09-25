#include <stdio.h>
#include <math.h>

void generateLinePoints(float x[2], float y[2], int num_points, FILE *ptr);
float dir(float a, float b, float c, float arr[2]);
float norm(float a, float b, float c, float arr[2]);
float dotproduct(int n, float vec1[2], float vec2[2]) ;

int main() {
    float a=0, b=1, c=-2 ;
    int n=2 ;
    float direction[2], normal[2] ;
    float x[2] = {0,2} ;
    float y[2] = {2,2} ;
    int num_points = 100;

    FILE *ptr = fopen("main.txt", "w");
    if (ptr == NULL) {
        perror("Error opening file");
        return 1;
    }
    dir(a, b, c, direction) ;
    norm(a, b, c, normal) ;
    generateLinePoints(x,y, num_points, ptr);
    fprintf(ptr, "%f, %f\n", direction[0], direction[1]);
    fprintf(ptr, "%f, %f\n", normal[0], normal[1]);
    fclose(ptr);

    printf("The points have been written to main.txt\n");
    printf("%f \n", dotproduct(n, direction, normal)) ;
    return 0;
}


