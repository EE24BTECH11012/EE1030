#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include "libs/matfun.h"
#include "libs/geofun.h"

void point_gen(FILE *fptr, double **A, double **B, int no_rows, int no_cols, int num_points) {
    for (double i = 0; i <= num_points; i++) {
        double **output = Matadd(A, Matscale(Matsub(B,A,no_rows,no_cols),no_rows,no_cols,(double)i/num_points), no_rows, no_cols);
        fprintf(fptr, "%lf,%lf\n", output[0][0], output[1][0]);
        freeMat(output,no_rows);
    }
}

void twoDtriangle_gen(double sideAB, double sideBC, double sideCA ) {
    double x[3], y[3] ;

    // Correct formula for angle A
    double angleA = acos(((sideAB * sideAB) + (sideCA * sideCA) - (sideBC * sideBC)) / (2 * sideAB * sideCA));

    x[0] = 0; y[0] = 0;
    x[1] = sideAB; y[1] = 0;
    x[2] = cos(angleA) * sideCA; y[2] = sin(angleA) * sideCA;

    int m = 2, n = 1;

    // Open the file for writing
    FILE *fptr = fopen("main.txt", "w");
    if (fptr == NULL) {
        printf("Error opening file!\n");
        return;  // Return early if file cannot be opened
    }

    // Create matrices for vertices
    double **A = createMat(m, n);
    double **B = createMat(m, n);
    double **C = createMat(m, n);

    A[0][0] = x[0];
    A[1][0] = y[0];
    B[0][0] = x[1];
    B[1][0] = y[1];
    C[0][0] = x[2];
    C[1][0] = y[2];

    // Generate points along the triangle's edges
    point_gen(fptr, A, B, m, n, 20);
    point_gen(fptr, B, C, m, n, 20);
    point_gen(fptr, C, A, m, n, 20);

    // Free allocated memory
    freeMat(A, m);
    freeMat(B, m);
    freeMat(C, m);

    // Close the file
    fclose(fptr);
}

