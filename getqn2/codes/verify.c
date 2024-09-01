#include <stdio.h>
#include <math.h>

int main()
{
	float x, y ;
	y = -3 - 2*x ;
	while ( x > 0 )
	{
		if (2*x + y + 3 == 0 )
		{
			break;
		}
		else
		{
			printf("The rank of the matrix is not one.\n");
		}

	}
	printf("The rank of the matrix is one.\n");
	return 0;
}

