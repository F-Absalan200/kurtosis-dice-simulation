# Version 1: Manual approach using custom choice array to select the 1/100 event.
# This version explicitly visualizes the 99% vs 1% probability distribution.


import numpy as np
import random


#later ver change probability to 99% and 1%
a = [0 for _ in range(99)] 
a.append(1)

dice = [i for i in range(1,7)]

def play(profit=0):
    result = np.random.choice(a)
    if result == 0:
        profit += int(np.random.choice(dice))
        return profit
    else:
        profit -= 350
        return profit
    
def test(num:int):
    profit = 0
    for _ in range(num):
        profit = play(profit)
        
    print(profit)
    
test(10000)