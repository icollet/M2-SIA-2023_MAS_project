from elements.Cell import Cell
from elements.Network import Network
from elements.Vehicle import Vehicle
from elements.Environment import Environment

import matplotlib.pyplot as plt


CONFIG = {
    "network_size": {"x": 4, "y": 3},
    "total_ticks": 100,
    "probabilities" : {"p_inf" : 0.2, "p_rep" : 0.2, "p_break" : 0.2},
    "vehicles": [
        {"id": 1, "position": (0, 0), "state": "Not infected"},
        {"id": 2, "position": (1, 2), "state": "Infected"},
        # ...
    ]
}


if __name__ == "__main__":
    environment = Environment(CONFIG)
    statistics = {}

    for tick in range(CONFIG["total_ticks"]):
        state_counts = environment.update_state()
        statistics[tick] = state_counts
        

        # Access the state counts for the current tick
        print(f"Tick {tick}: {state_counts}")
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
