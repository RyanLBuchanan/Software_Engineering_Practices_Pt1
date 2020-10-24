# Software Engineering Practices Pt 1 tutorial from Machine Learning Engineering Nanodegree - Udacity -> Input by Ryan L Buchanan 24OCT20

import math
import numpy as np
import matplotlib.pyplot as plt

def flat_curve(arr, n):
    return [i + n for i in arr]

def square_root_curve(arr):
    return [math.sqrt(i) * 10 for i in arr]

test_scores = [88, 92, 79, 93, 85]

def sorted_test_scores(arr):
    return test_scores.sort()


curved_5 = flat_curve(test_scores, 5)
curved_10 = flat_curve(test_scores, 10)
curved_sqrt = square_root_curve(test_scores)

for score_list in test_scores, curved_5, curved_10, curved_sqrt:
    print(np.mean(score_list))
    
for score_list in test_scores, curved_5, curved_10, curved_sqrt:
    print(score_list)

plt.plot(test_scores)
plt.ylabel('Test scores')
plt.show()

# List of Integers 
numbers = [1, 3, 4, 2] 
  
# Sorting list of Integers 
numbers.sort() 

print(numbers)
