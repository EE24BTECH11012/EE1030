#include <stdio.h>
#include <math.h>

void generateLinePoints(float x1, float y1, float x2, float y2, int num_points, FILE *ptr);
float dir(float x1, float y1, float x2, float y2);
float norm(float x1, float y1, float x2, float y2);

int main() {
    float x1 = 2, x2 = 0, y1 = 0, y2 = 2;
    int num_points = 20;

    FILE *ptr = fopen("main.txt", "w");
    if (ptr == NULL) {
        perror("Error opening file");
        return 1;
    }
    
    generateLinePoints(x1, y1, x2, y2, num_points, ptr);
    fprintf(ptr, "%f\n", dir(x1, y1, x2, y2));
    fprintf(ptr, "%f\n", norm(x1, y1, x2, y2));
    fclose(ptr);

    printf("The points have been written to main.txt\n");
    return 0;
}

void generateLinePoints(float x1, float y1, float x2, float y2, int num_points, FILE *ptr) {
    for (int i = 0; i <= num_points; i++) {
        float t = (float)i / num_points;
        float x = x1 * (1 - t) + x2 * t;
        float y = y1 * (1 - t) + y2 * t;
        fprintf(ptr, "%f %f\n", x, y);
    }
}

float dir(float x1, float y1, float x2, float y2) {
    return (float)(y2-y1)/(float)(x2-x1) ;
}

float norm(float x1, float y1, float x2, float y2) {
    return (float)(x1-x2)/(float)(y2-y1) ;
}

