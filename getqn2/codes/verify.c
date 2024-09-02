#include <stdio.h>

// Function to compute the determinant of a 3x3 matrix
int determinant(int x1, int y1, int x2, int y2, int x3, int y3) {
    return x1 * (y2 - y3) - y1 * (x2 - x3) + (x2 * y3 - x3 * y2);
}

// Function to check if three points are collinear
int areCollinear(int x1, int y1, int x2, int y2, int x3, int y3) {
    // Calculate the determinant
    int det = determinant(x1, y1, x2, y2, x3, y3);
    
    // If the determinant is zero, the points are collinear
    return det == 0;
}

int main() {
    int x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6;

    x1 = -5, y1 = 7;
    x2 = -4, y2 = 5;
    x3 = -6, y3 = 9;
    x4 = 0, y4 = -3;
    x5 = 1, y5 = -5;
    x6 = 2, y6 = -7;

    // Check if the points are collinear
    if (areCollinear(x1, y1, x2, y2, x3, y3)) {
        printf("The points (%d, %d), (%d, %d), and (%d, %d) are collinear.\n", x1, y1, x2, y2, x3, y3);
    } else {
        printf("The points (%d, %d), (%d, %d), and (%d, %d) are not collinear.\n", x1, y1, x2, y2, x3, y3);
    }

 if (areCollinear(x1, y1, x2, y2, x4, y4)) {
        printf("The points (%d, %d), (%d, %d), and (%d, %d) are collinear.\n", x1, y1, x2, y2, x4, y4);
    } else {
        printf("The points (%d, %d), (%d, %d), and (%d, %d) are not collinear.\n", x1, y1, x2, y2, x4, y4);
    }

 if (areCollinear(x1, y1, x2, y2, x5, y5)) {
        printf("The points (%d, %d), (%d, %d), and (%d, %d) are collinear.\n", x1, y1, x2, y2, x5, y5);
    } else {
        printf("The points (%d, %d), (%d, %d), and (%d, %d) are not collinear.\n", x1, y1, x2, y2, x5, y5);
    }
 if (areCollinear(x1, y1, x2, y2, x6, y6)) {
        printf("The points (%d, %d), (%d, %d), and (%d, %d) are collinear.\n", x1, y1, x2, y2, x6, y6);
    } else {
        printf("The points (%d, %d), (%d, %d), and (%d, %d) are not collinear.\n", x1, y1, x2, y2, x6, y6);
    }

   

    return 0;
}

