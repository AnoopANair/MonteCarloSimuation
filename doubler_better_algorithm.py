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

# doubler better algorithm

# each time i lose, i double my wager amount

def bet_doubler(funds,initial_wager,wager_count,color):
    global dbust
    global dprof
    value=funds
    prevwager=initial_wager
    vY=[]
    vX=[]
    current_wager=0
    prevres="win"
    wager=prevwager
    while current_wager< wager_count:
        if prevres=="win":
            if diceroll():
                wager=prevwager
                value+=wager
                vY.append(value)
                vX.append(current_wager)
            else:
                wager=prevwager
                value-=wager
                prevres="loss"
                prevwager=initial_wager
                wager=prevwager
                vX.append(current_wager)
                vY.append(value)
                if value<=0:
                    dbust+=1
                    break
                    
        elif prevres=="loss":
            if diceroll():
                prevwager=2*prevwager
                wager=prevwager
                if (value-wager<0):
                    wager=value
                value+=wager
                prevres='win'
                vX.append(current_wager)
                vY.append(value)
                wager=initial_wager
                wager=prevwager
            else:
                prevwager=2*prevwager
                wager=prevwager
                if (value-wager<0):
                    wager=value
                value-=wager
                prevres='loss'
                vY.append(value)
                vX.append(current_wager)
                if value<=0:
                    dbust+=1
                    break                
        current_wager+=1
    plt.plot(vX,vY,color)
    if (value > funds):
        dprof+=1
        
x=0
dbust=0
dprof=0

while x<=sampleSize:
    bet_doubler(strfund,wagersie,wgercount,'c')
    x+=1
    
print("double better bust chance", (dbust/sampleSize)*100)
print("double better profit chance", (dprof/sampleSize)*100)
plt.ylabel("value")
plt.xlabel("count")
plt.axhline(0,color='r')
plt.show()
    
    
    
