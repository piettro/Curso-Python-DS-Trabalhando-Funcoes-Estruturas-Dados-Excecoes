import matplotlib.pyplot as plt
from random import choice

students =['John','Mary','Joseph','Anie']
records =[8.5, 9, 6.5,7.0]

print(choice(students))

plt.bar(x=students,height=records)
plt.show()