import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
''' 
T_null=np.array([[ 1.,  2.,  3.,  4.,  5.,0.],
                 [ 1.,  2.,  3.,  4.,  5.,0.],
                 [ 1.,  2.,  3.,  4.,  5.,0.],
                 [ 1.,  2.,  3.,  4.,  5.,0.],
                 [ 1.,  2.,  3.,  4.,  5.,0.],
                 [ 1.,  2.,  3.,  4.,  5.,0.],
                 ])

T_null = np.array([[ 1./6.,  1./6.,  1./6.,  1./6.,  1./6.,1./6.],
                 [ 1./6.,  1./6.,  1./6.,  1./6.,  1./6.,1./6.],
                 [ 1./6.,  1./6.,  1./6.,  1./6.,  1./6.,1./6.],
                 [ 1./6.,  1./6.,  1./6.,  1./6.,  1./6.,1./6.],
                 [1./6.,  1./6.,  1./6.,  1./6.,  1./6.,1./6.],
                 [ 1./6.,  1./6.,  1./6.,  1./6.,  1./6.,1./6.]])
'''



T_full= np.array([[ 1./6.,  1./6.,  1./6.,  1./6.,  1./6.,0],
                 [ 1./6.,  1./6.,  1./6.,  1./6.,  1./6.,0],
                 [ 1./6.,  1./6.,  1./6.,  1./6.,  1./6.,0],
                 [ 1./6.,  1./6.,  1./6.,  1./6.,  1./6.,0],
                 [1./6.,  1./6.,  1./6.,  1./6.,  1./6.,0],
                 [ 1./6.,  1./6.,  1./6.,  1./6.,  1./6.,0]])

def SetTransitionMatrix_NULL():
    T_null = np.zeros((104,104))
    prob = 1./6.
    n = 0
    for i in range(0,104):
       # T_null[row,col]
       T_null[i,n:n+6] = prob
       n = n + 1

       if np.sum(T_null[i,:]) == 1/ 6:
           T_null[i,-1] = prob * 6 #setting last state too 1

       elif np.sum(T_null[i,:]) == 2/ 6 :
           T_null[i, -1] = prob * 5

       elif np.sum(T_null[i,:]) == 3/ 6:
           T_null[i, -1] = prob * 4

       elif np.sum(T_null[i, :]) == 4 / 6:
           T_null[i, -1] = prob * 3
           T_null[-5, -1] = prob * 2
           T_null[-5, -2] = prob * 1
           #print(T_null[-5, :], 'running')

       elif np.sum(T_null[i, :]) == 5. / 6.:

           T_null[i, -1] = prob * 2
           T_null[i, -2] = prob * 1
           #print(T_null[i, :], 'running 123')







    return T_null
#print(SetTransitionMatrix_NULL())
#Visual Verification
sns.heatmap(SetTransitionMatrix_NULL())
#plt.show()
T_null = SetTransitionMatrix_NULL()
###Trying to find an approx way to iteratively play but Cant figure out how to randomize the dice and incorpperate it with the Tmatrix
def Probably():
    p = np.zeros((1, 104))
    p[0, 0] = 1
    print("before")

    for i in range(1,100):
        print('running')
        #p = p.dot(SetTransitionMatrix_NULL())
        p = (SetTransitionMatrix_NULL() - 1)*np.linalg.inv(SetTransitionMatrix_NULL())
        '''  
        max_probability = max(p[0, 0:]) #finding max value
        Probable_turn = np.argmax(p) #finding max value index value
        P = []
        P.insert(Probable_turn, 1)
        #if Probable_turn = 4
        #do this
        if i is 99:
            max_probability = max(p[0,0:])
            Probable_turn = np.argmax(p)
            #print (p)
            #print (max_probability,Probable_turn )
        '''
        return p
a = Probably()
#print(a)
sns.heatmap(a)
#plt.show()

'''   
print(p)
sns.heatmap(p,vmin=0, vmax=.65, center = .5, annot=True)
plt.show()
print("working")
'''

#todo
#use a function to set it or by hand up top, your choice.