import numpy as np

A = np.array([[3.45 +0.98j, 0.009+4.56j],
             [3.45 + 0.76j, -2.45+5.64j]])

print(np.linalg.eigvals(A))
