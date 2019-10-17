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
lower_bust=31.235#lower limit of going broke
higher_profit=40 #upper limit of profit

#multiple better alogorithm



# if i lose , i will bet m times of my previous wageramount



def bet_multiple(funds,initial_wager,wager_count):
    global mbust
    global mprof
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
                    mbust+=1
                    break
                    
        elif prevres=="loss":
            if diceroll():
                prevwager=m*prevwager
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
                prevwager=m*prevwager
                wager=prevwager
                if (value-wager<0):
                    wager=value
                value-=wager
                prevres='loss'
                vY.append(value)
                vX.append(current_wager)
                if value<=0:
                    mbust+=1
                    break
                    
               
        current_wager+=1

    if (value > funds):
        mprof+=1
# finding the best multiple through monte carlo 
while True:
    mss=1000
    mbust=0
    mprof=0
    m=rnd.uniform(0.1,10.0)
    cms=1
    while cms<mss:
        bet_multiple(strfund,wagersie,wgercount)
        cms+=1
    if ((mbust/mss)*100.00 < lower_bust) and ((mprof/mss)*100.00 > higher_profit):
        print ("########################")
        print ("m winner= ", m)
        print ("lowerbust=", lower_bust)
        print ("higher_profit", higher_profit)
        print ("bust rate=",(mbust/mss)*100.00)
        print ("profit rate =",(mprof/mss)*100.00)
        print ("########################")
    else :
        print ("########################")
        print ("m loser= ", m)
        print ("lowerbust=", lower_bust)
        print ("higher_profit", higher_profit)
        print ("bust rate=",(mbust/mss)*100.00)
        print ("profit rate =",(mprof/mss)*100.00)
        print ("########################")
        pass
