# imports

import numpy as np
import random as rnd
import matplotlib
import matplotlib.pyplot as plt
import time


# random number generator for dice roll simulation

def diceroll():
    roll = rnd.randint(1,100)
    if roll==100:
        return False
    elif roll<=50:
        return False
    elif 100>roll>50:
        return True
    
#predefined constants
    
sampleSize=1000  #sample size
strfund=10000    #starting funds
wagersie=100     #wagersize
wgercount=1000   #wagercount

# A simple better


def simple_bet(funds,inital_wager,wager_count,color):
    global sbust
    global sprof
    value=funds
    wager=inital_wager
    vY=[]
    wX=[]
    current_wager=0
    while current_wager<wager_count:
        
        if diceroll():
            value += wager
            vY.append(value)
            wX.append(current_wager)
        else:
            value -= wager
            vY.append(value)
            wX.append(current_wager)
        current_wager+=1
    if value<=0:
        sbust+=1
    plt.plot(wX,vY,color)
    if (value > funds):
        sprof+=1
   
x=0
sbust=0
sprof=0
while x<=sampleSize:
    simple_bet(strfund,wagersie,wgercount,'c')
    x+=1
print("simple better bust chance", (sbust/sampleSize)*100)
print("simple better profit chance", (sprof/sampleSize)*100)
plt.ylabel("value")
plt.xlabel("count")
plt.axhline(0,color='r')
plt.show()
