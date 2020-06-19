import numpy as np
import matplotlib.pyplot as plt

def mounty_hall():
    plt.style.use('seaborn-whitegrid')

    n_trials = 1000

    prizes = np.random.randint(0, 3, size=(n_trials))
    first_choices = np.random.randint(0, 3, size=(n_trials))

    switching_player_gains = (prizes != first_choices).astype(int)
    keeping_player_gains = (prizes == first_choices).astype(int)
    plot = plt.bar([1, 2], [switching_player_gains.sum(),
                            keeping_player_gains.sum()],
                            tick_label=["Change", "Stay"])
    plt.show()