
from TransitionMatrix import T_a
from TransitionMatrix import T_b
from TransitionMatrix import p_a
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns

#print(T_b) #testing matrices calling

#checking that the sum of the rows are 1
for n in range (0,5):
    if np.sum(T_a[n,:]) > 1: #selecting the entire row n
        print("The Matrices Probabilities for T_a are greater than 1, in row %d" % n)
    elif np.sum(T_a[n,:]) < 1:
        print("The Matrices Probabilities for T_a are less than 1 in row %d" % n)


for n in range (0,9):

    if np.sum(T_b[n,:]) > 1:
        print("The Matrices Probabilities for T_b are greater than 1, in row %d" % n)
    elif np.sum(T_b[n,:]) < 1:
        print("The Matrices Probabilities for T_b are less than 1 in row %d" % n)
"""    #testing    
mrcarlo = random.uniform(0,1)
matrix = T_a
n =0
print(matrix[n,0:])
print(mrcarlo,"mrcarlo")
mrscarlo = np.abs((matrix[n,0:] - mrcarlo)).argmin() #finding the closest in the row
print(mrscarlo, "mrscarlo")
print("go go go go "
      ""
      ""
      ""
      "/n")

mrcarlo = .30
matrix = T_a
n =0
print(matrix[0,n:])
print(mrcarlo,"mrcarlo")
mrscarlo = np.abs((matrix[n,0:] - mrcarlo)).argmin() #finding the closest in the row
print(mrscarlo,'mrscarlo')
y = np.zeros((1,5))
y = ["state1", "state2", "state3", "state4", "state5"]
print (y)

x = np.random.choice( y , 1, p = matrix[n, 0:])
print(x , 'printing the choice')
"""

def carlo(): #partA
    n = 0
    carlo_list = []

    for i in range(1,100):
        carlo_list.insert(i,n)
        mrcarlo = random.uniform(1, 100)  # randomly drawing numbers


        if n == 0:#first state
            if mrcarlo < 50:
                n = 0
            elif 50 < mrcarlo < 60:
                n = 1
            elif 60 < mrcarlo < 70:
                n = 2
            elif 70 < mrcarlo < 85:
                n = 3
            else:
                n =4
        elif n == 1:
            n = 0
        elif n == 2:
            if mrcarlo < 75:
                n = 0
            else:
                n = 2
        elif n == 3:
            if mrcarlo < 25:
                n = 0
            else:
                n = 3
        else:
            if mrcarlo < 30:
                n = 0
            else:
                n = 4
    return carlo_list

def monte(): #partB
    n = 0
    monte_list = []
    for i in range(1,100):
        monte_list.insert(i,n)
        mrcarlo = random.uniform(1,100) #randomly drawing numbers

        if n == 0: #first state

            if mrcarlo < 10:
                n = 0
            elif 10 < mrcarlo < 20:
                n = 1
            elif 20 < mrcarlo < 30:
                n = 2
            elif 30 < mrcarlo < 40:
                n = 3
            elif 40 < mrcarlo < 50:
                n = 4
            elif 50 < mrcarlo < 60:
                n = 5
            elif 60 < mrcarlo < 70:
                n = 6
            elif 70 < mrcarlo < 80:
                n = 7
            elif 80 < mrcarlo < 100:
                n = 8
        elif n == 1:
            if mrcarlo < 1/3*100:
                n = 0
            elif 1/3*100 < mrcarlo < 2/3*100:
                n = 2
            elif 2/3*100 < mrcarlo < 100:
                n = 6
        elif n == 2:
            if mrcarlo < 100/3:
                n = 2
            else:
                n = 5
        elif n == 3:
            if mrcarlo < 25:
                n = 0
            else:
                n = 6
        elif n == 4:
            if mrcarlo < 30:
                n = 0
            elif 30 < mrcarlo < 70:
                n = 1
            else:
                n = 4
        elif n == 5:
            if mrcarlo < 10:
                n = 0
            else:
                n = 5
        elif n == 6:
            if mrcarlo < 20:
                n = 0
            elif 20 < mrcarlo < 40:
                n = 2
            elif 40 < mrcarlo < 60:
                n =4
            elif 60 < mrcarlo < 80:
                n = 6
            else:
                n = 8
        elif n == 7:
            if mrcarlo < 50:
                n = 0
            else:
                n = 8
        else:
            if mrcarlo < 30:
                n = 1
            elif 30 < mrcarlo < 35:
                n = 3
            elif 35 < mrcarlo < 40:
                n = 4
            elif 40 < mrcarlo < 70:
                n = 6
            elif 70 < mrcarlo < 90:
                n = 7
            else:
                n = 8
    return monte_list
carl = [carlo()]
mrmonte = [monte()]
print(carl)
print(mrmonte)
sns.heatmap(carl,cmap="YlGnBu", xticklabels= 20 , yticklabels= False)
plt.xlabel('iterations')
plt.title('Monte Carlo Iteration Heat Map Part A')
plt.show()

sns.heatmap(mrmonte,cmap="YlGnBu", xticklabels= 20 , yticklabels= False)
plt.xlabel('iterations')
plt.title('Monte Carlo Iteration Heat Map Part B')
plt.show()
#partb pdf is the last value of the pmatrix so track the last value over its iterated
#