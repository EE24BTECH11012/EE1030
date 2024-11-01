import numpy as np
import matplotlib.pyplot as plt

schoolA = [2014, 2015, 2016, 2017, 2018]
#student = [1,2,3,4,5,6,7,8,9,10]
no_studentsA = [3, 5, 5, 6, 4]
no_studentsB = [4, 7, 8, 7, 5]
xpos = np.arange(len(schoolA))

plt.bar(xpos-0.2, no_studentsA, width=0.4, color='red', label="School A")
plt.bar(xpos+0.2, no_studentsB, width=0.4, color='blue', label="School B")
plt.xticks(xpos, schoolA)
plt.yticks(np.arange(10,10,10))
#plt.ylabel("Number of students")
plt.legend()
plt.grid(axis='y')
plt.savefig('../figs/fig.png', format='png', bbox_inches='tight')
plt.show()
