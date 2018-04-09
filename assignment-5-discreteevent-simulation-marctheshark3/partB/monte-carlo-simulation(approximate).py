
import numpy as np
from scipy.interpolate import UnivariateSpline
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import scipy.stats as st
import TransitionMatrix as TM
from TransitionMatrix import SetTransitionMatrix_NULL

def configuration(m,spaces):
    if m == 1:

        if spaces == 4:
            spaces = 20
        elif spaces == 17 or spaces == 24:
            spaces = 38
        elif spaces == 37:
            spaces = 48
        elif spaces == 42:
            spaces = 15
        elif spaces == 62 or spaces == 69:
            spaces = 71
        elif spaces == 84:
            spaces = 92
        elif spaces == 97:
            spaces = 94
        return spaces
    elif m == 2:
        if spaces == 4:
            spaces = 13
        elif spaces == 17 or spaces == 24:
            spaces =30
        elif spaces == 37:
            spaces = 48
        elif spaces == 42:
            spaces = 15
        elif spaces == 62 or spaces == 69:
            spaces = 55
        elif spaces == 84:
            spaces = 75
        elif spaces == 97:
            spaces = 70
        return spaces
    else:
        spaces = spaces



def num_gen(m):
    turn_stats = []  # setting turn_stats for every game
    spaces = 0
    turns = 0
    move_bank = []
    i = 0
    #while turns < 104:
    for turns in range(1,500):

       dice = np.random.randint(1, 6)

        # to keep track out how mant turns it takes
       move_bank.insert(turns, dice)
       #print(spaces,"spaces")
       #print(dice,"dice",turns,"turns")
       i = i + 1
       if dice == 1:
           #print("beforeinside",spaces)
           spaces  = spaces + dice
           #print("afterinside", spaces)
           configuration(m, spaces)
           if spaces > 104:
               #print('broken', turns)
               turn_stats.insert(i, turns)
               break

       elif dice == 2:
           #print("beforeinside", spaces)
           spaces = spaces + dice
           #print("afterinside", spaces)
           configuration(m, spaces)
           if spaces > 104:
               #print('broken', turns)
               turn_stats.insert(i, turns)
               break

           # elif spaces > 104:
            #    print("breaking the law", turns)
            #    turn_stats.insert(i, turns)  # adding only to count turns
            #   break

       elif dice == 3:
            #print("beforeinside", spaces)
            spaces = spaces + dice
            #print("afterinside", spaces)
            configuration(m, spaces)
            if spaces > 104:
                #print('broken', turns)
                turn_stats.insert(i, turns)
                break

            # elif spaces > 104:
            #    print("breaking the law", turns)
            #    turn_stats.insert(i, turns)  # adding only to count turns
            #   break

       elif dice == 4:

            #print("beforeinside", spaces)
            spaces = spaces + dice
            #print("afterinside", spaces)
            configuration(m, spaces)
            if spaces > 104:
                #print('broken', turns)
                turn_stats.insert(i, turns)
                break

            # elif spaces > 104:
            #    print("breaking the law", turns)
            #    turn_stats.insert(i, turns)  # adding only to count turns
            #   break

       elif dice == 5:
            #print("beforeinside", spaces)
            spaces = spaces + dice
            #print("afterinside", spaces)
            configuration(m, spaces)
            if spaces > 104:
                #print('broken', turns)
                turn_stats.insert(i, turns)
                break

            # elif spaces > 104:
            #    print("breaking the law", turns)
            #    turn_stats.insert(i, turns)  # adding only to count turns
            #   break
       elif dice == 6:
            #print("beforeinside", spaces)
            spaces = spaces + 0
            #print("afterinside", spaces)
            configuration(m, spaces)
            if spaces > 104:
                #print('broken', turns)
                turn_stats.insert(i, turns)
                break

    return (turn_stats)

def game_analysis(config):
        turns_to_win = []

        for game in range(1,101):

            turns_to_win.insert(game,num_gen(config))

            #print (turns)

        return (turns_to_win)



def run_this(zero,dist):

    a = game_analysis(zero)
    a.sort() #sorting list


    avg = np.mean(a)
    std = np.std(a)
    print(avg,'mean')
    mode = st.mode(a)
    print(mode[0],'mode')
    #print(avg,std)
    #if dist == 'pdf':
    num_bins = 10
    n, bins, patches = plt.hist(a, num_bins, normed=1, facecolor='green', alpha=0.5)
    y = mlab.normpdf(bins, avg, std)
    plt.plot(bins, y, 'r--')

    if zero == 1:
        plt.xlabel('Turns to Win: Configuration 1')
    elif zero == 2:
        plt.xlabel('Turns to Win: Configuration 2')
    else:
        plt.xlabel('Turns to Win')
    plt.ylabel('Probability')
    plt.title("Cumalative Density Function: Monte Carlo")
    plt.show()
    #elif dist == 'cdf':
    num_bins = 10

    fig, ax = plt.subplots(figsize=(8, 4))
    n, bins, patches = ax.hist(a, num_bins, normed=1, histtype='step', cumulative=True)
    y = mlab.normpdf(bins, avg, std).cumsum()
    y /= y[-1]
    ax.plot(bins, y, 'k--', linewidth=1.5)

    if zero == 1:
        plt.xlabel('Turns to Win: Configuration 1')
    elif zero == 2:
        plt.xlabel('Turns to Win: Configuration 2')
    else:
        plt.xlabel('Turns to Win')
    plt.ylabel('Probability')
    plt.title("Cumulative Density Function: Monte Carlo")
    plt.show()

run_this(3,'cdf')

