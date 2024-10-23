float mp(float num1, float num2)
{
	return (2*num1) - num2 ;
}

float f1(float num1, float num2)
{
	return num1 + 5.0 ;
}

float f2(float num1, float num2)
{
	return num2 - 10.0 ;
}

int determinant(int matrix[3][3])
{
    int det;
    
    det = matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]);
    
    return det;
}

