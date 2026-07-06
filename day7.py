numbers = [10,20,40,50,60]

# output = [15,25,45...]

result = []


for number in numbers:
    result.append(number+5)

print(result)


import numpy as np
numbers = np.array([10,20,30,40,50])
print(numbers+5)