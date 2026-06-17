# Version 2: More Pythonic and optimized approach.
# Directly utilizes NumPy's built-in random integer generation for cleaner logic.

import random as rd

hundredfaced_dice = [0, 1]
population = [99, 1]
dice = [1, 2, 3, 4, 5, 6]
def play():
    first_luck = rd.choices(hundredfaced_dice, population)

    if first_luck[0] == 0:
        return rd.choice(dice)
    else:
        return -350
    
def test(number):
    profit = 0
    for _ in range(number):
        profit += play()
        
    return profit

print(test(10))