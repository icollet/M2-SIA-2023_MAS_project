from elements.Cell import Cell
from elements.Network import Network
from elements.Vehicle import Vehicle
from elements.Environment import Environment

import matplotlib.pyplot as plt
import random


import random

CONFIG = {
    "network_size": {"x": 100, "y": 100},
    "total_ticks": 100,
    "probabilities" : {"p_inf" : 0.2, "p_rep" : 0.3, "p_break" : 0.7},
    "seed" : 10,
    "vehicles": [
        {"id": i+1, "position": (i%100, i//100), "state": random.choice(["Not infected", "Infected"])} for i in range(50)
    ]
}
if __name__ == "__main__":
    environment = Environment(CONFIG)
    statistics = {}

    for tick in range(CONFIG["total_ticks"]):
        state_counts = environment.update_state()
        statistics[tick] = state_counts
        vehicles = environment.vehicles
        cells_list = environment.network.cells


        # Access the state counts for the current tick
        # ...

    # Plotting the statistics
    x = []
    infected = []
    not_infected = []
    repaired = []
    broken_down = []
    for tick in range(CONFIG["total_ticks"]):
        x.append(tick)
        infected.append(statistics[tick]["Infected"])
        not_infected.append(statistics[tick]["Not infected"])
        repaired.append(statistics[tick]["Repaired"])
        broken_down.append(statistics[tick]["Broken down"])

    plt.plot(x, infected, label='Infected')
    plt.plot(x, not_infected, label='Not infected')
    plt.plot(x, repaired, label='Repaired')
    plt.plot(x, broken_down, label='Broken down')
    
    plt.xlabel('tick')
    plt.ylabel('number of vehicles')
    plt.title('State of the vehicles in the network')
    plt.legend()

    plt.show()
