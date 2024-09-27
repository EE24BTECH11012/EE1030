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

    fprintf(ptr, "%lf\n", Area(n, centre, otherPoint));
    fclose(ptr); // Always good to close the file
    printf("The values have been printed to main.txt\n");

    return 0;
}
