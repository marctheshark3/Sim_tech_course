import numpy as np



T_a = np.array([[ .5,  .1,  .1,  .15,  .15],
               [  1,   0,   0,    0,    0],
               [.75,   0,   0,  .25,    0],
               [.25,   0,   0,  .75,    0],
               [ .3,   0,   0,    0,   .7]])



T_b =np.array( [  [ .1,  .1,  .1,  .1,  .1,  .1,  .1,  .1,  .2],
                 [1./3.,   0, 1./3.,   0,   0,   0, 1./3.,   0,   0],
                 [  0,   0, 1/3,   0,   0, 2/3,   0,   0,   0],
                 [1/4,   0,   0,   0,   0,   0, 3/4,   0,   0],
                 [0.3, 0.4,   0,   0, 0.3,   0,   0,   0,   0],
                 [0.1,   0,   0,   0,   0, 0.9,   0,   0,   0],
                 [0.2,    0, 0.2,  0, 0.2,   0, 0.2,   0, 0.2],
                 [0.5,    0,   0,  0,   0,   0,   0,   0, 0.5],
                 [  0,  0.3,  0,0.05,0.05,   0, 0.3, 0.2, 0.1]   ] )

p_a = np.zeros((1,5))
p_a[0,0]=1
#print(p_a)




p_b = np.zeros((1,9))#creating random matrix 1 X 9
p_b[0,0] = 1
#print(p_b,"pb")

#print(p_b.dot(T_b))

#def SetTransitionMatrix_PartA():
#todo
#use a function to set it or by hand up top, your choice.

'''  
#in class
T = np.zeros((10,10))

Slides = [(0,2),(0,4)]

prop = 1./7.
for s in Slides:
    T[s] = prob

p = np.zeros(10)
p.dot(T)

for in range nlah
    p^(k+1)= p^k * T

    return some p vector

if p<10 snd p>20 :
    do this
elif p<20 and p<30:
    do this
else:
'''