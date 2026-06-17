# Version 1: Manual approach using custom choice array to select the 1/100 event.
# This version explicitly visualizes the 99% vs 1% probability distribution.

import numpy as np

a = [0 for _ in range(99)] 
a.append(1)
dice = [i for i in range(1,7)]

def play():
    result = np.random.choice(a)
    if result == 0:
        return int(np.random.choice(dice))
    else:
        return -350
    
def test(num: int):
    profit = 0
    for _ in range(num):
        profit += play()
    print(profit)
    
if __name__ == '__main__':
    test(10000)