# Version 2: More Pythonic and optimized approach.
# Directly utilizes NumPy's built-in random integer generation for cleaner logic.

import numpy as np
import matplotlib.pyplot as plt

def run_dice_simulation(num_simulations=50000):
    steps = num_simulations
    cash = 0
    cash_sequence = [0]
    game_elements = [-350, 'ordinary_dice']
    probabilities = [0.01, 0.99]

    for i in range(steps):
        result = np.random.choice(game_elements, p=probabilities)
        if result == -350:
            cash -= 350
            cash_sequence.append(cash)
        else:
            ordinary_dice = np.random.randint(1, 7)
            cash += ordinary_dice
            cash_sequence.append(cash)
    return cash_sequence

if __name__ == '__main__':
    cash_sequence = run_dice_simulation()
    plt.plot(cash_sequence)
    plt.show()