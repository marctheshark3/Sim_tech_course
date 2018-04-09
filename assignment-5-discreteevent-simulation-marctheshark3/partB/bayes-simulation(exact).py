import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats
import TransitionMatrix as TM

import TransitionMatrix as TM









def null():
    from TransitionMatrix import T_full
    from TransitionMatrix import T_null
    # do I need to use transition matrix for moves or spaces in the game???
    p = np.zeros((1, 104))
    p[0, 0] = 1


    for i in range(1,100):

        p = p.dot(T_null)

    return p

def null_works():
    from TransitionMatrix import T_null
    Q = T_null[:-1,:-1]
    I = np.eye(103)
    N = np.linalg.inv(I - Q)
    Sol = N.dot(np.ones(103)).ravel()[0]
    print ('Null test' , Sol, 'turns' )
    return Sol
#null_works()

from TransitionMatrix import T_null
P = T_null

# Found online
def move(state, P):
    possible = P[state, :].nonzero()[0]
    probs = P[state, possible].cumsum()
    return possible[probs >= np.random.rand()].min()

def play_chutes_and_ladders(P):
    """
    Play a game of chutes and ladders, return the number of moves.

    P -- transition matrix
    """

    # initialize the game
    state = 0
    moves = 0

    while state < 104 :
        state = move(state, P)
        moves += 1

    return moves

# run a bunch of simulations and find out the average number of moves
N = 100
results = np.array([play_chutes_and_ladders(P) for _ in range(N)])
print ('mean moves to finish', results.mean())

print( play_chutes_and_ladders(P))


