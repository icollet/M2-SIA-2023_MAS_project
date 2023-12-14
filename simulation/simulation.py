from elements.Cell import Cell
from elements.Network import Network
from elements.Vehicle import Vehicle
from elements.Environment import Environment

from ui.main_window import VehicleGridApp

import tkinter as tk
import matplotlib.pyplot as plt
import random

import time

CONFIG = {
    "network_size": {"x": 15, "y": 15},
    "delay": 0.5,
    "total_ticks": 100,
    "probabilities" : {"p_inf" : 0.9, "p_rep" : 0, "p_break" : 0},
    "seed" : 10,
    "vehicles": [
        # {"id": i+1, "position": (i%20, i//20), "state": random.choice(["Not infected", "Infected"])} for i in range(40)
    ]
}


def generate_vehicles(num_vehicles, infection_rate, grid_size):
    vehicles = []
    cells = [(x, y) for x in range(grid_size) for y in range(grid_size)]
    
    n_infected = int(infection_rate / 100 * num_vehicles)
    i = 0
    while i < n_infected:
        cell = random.choice(cells)
        cells.remove(cell)
        vehicles.append({"id": i+1, "position": cell, "state": "Infected"})
        i += 1
    while i < num_vehicles:
        cell = random.choice(cells)
        cells.remove(cell)
        vehicles.append({"id": i+1, "position": cell, "state": "Not infected"})
        i += 1
    
    return vehicles


def launch():
    root = tk.Tk()
    root.title("Simulation de Mobilité")

    app = VehicleGridApp(root)
    app.pack()

    num_vehicles_entry = tk.Entry(root)
    num_vehicles_entry.pack()

    infection_rate_entry = tk.Entry(root)
    infection_rate_entry.pack()

    def start_simulation():
        num_vehicles = int(num_vehicles_entry.get())
        infection_rate = float(infection_rate_entry.get())
        vehicles = generate_vehicles(num_vehicles, infection_rate, app.grid_size)
        CONFIG["vehicles"] = vehicles

        environment = Environment(CONFIG)
        statistics = {}

        loop(environment, statistics, app)
        #app.update_vehicles(vehicle_states)

    start_button = tk.Button(root, text="Démarrer la Simulation", command= start_simulation)
    start_button.pack()

    root.mainloop()


def loop(environment, statistics, app):

    for tick in range(CONFIG["total_ticks"]):
        print("STATE AT TICK :", tick)
        #environment.network.print_cell_content()
        state_counts = environment.update_state()
        statistics[tick] = state_counts
        vehicles = environment.vehicles
        print(len(vehicles))
        cells_list = environment.network.cells

        app.update_vehicles(vehicles)

        time.sleep(CONFIG["delay"])

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

if __name__ == "__main__":

    launch()

    