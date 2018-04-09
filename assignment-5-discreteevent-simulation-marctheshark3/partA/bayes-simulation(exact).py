from TransitionMatrix import T_a
from TransitionMatrix import T_b
from TransitionMatrix import p_a
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

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

#simulation a
def sima():
    from TransitionMatrix import p_a
    counter = 0
    while counter < 100:
       #print("running a", counter)
        p_a = (p_a).dot(T_a)
        counter = counter + 1
    return p_a

def simb():

    from TransitionMatrix import p_b
    counter = 0
    while counter < 100:
        #print("running b", counter)
        p_b = (p_b).dot(T_b)
        #print(p_b)
        counter = counter + 1
        '''   
        if counter is 100:
            #maxprob = max(p_b["col" 0 ,"row" max(:)])
            print("max " ,max(p_b[0,0:]))
        '''
        p_3 = [p_b[0,0:3],p_b[0,3:6],p_b[0,6:9]]
    return p_3

sim1 = sima()
sim2 = simb()

print(sim1,"part A")
print(sim2,"part B")

sns.heatmap(sim1,vmin=0, vmax=.65, center = .5, yticklabels=False)
plt.xlabel('states')

plt.title('Bayesian Heat Map 1 X 5')
plt.show()

sns.heatmap(sim2,vmin=0, vmax=.65, center = .5, annot=True,yticklabels=False,xticklabels=False)
plt.title("Bayesian Heat Map 3x 3")
plt.show()





#print(parta)


