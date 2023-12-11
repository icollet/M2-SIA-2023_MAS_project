from elements.Cell import Cell
from elements.Network import Network
from elements.Vehicle import Vehicle

import random


class Environment:
    def __init__(self, config):
        self.network = self.create_network(config)
        self.vehicles = self.create_vehicles(config)
        self.tick_stats = {"Infected": [], "Not infected": [], "Repaired": [], "Broken down": []}
        self.seed = config["seed"]
        random.seed(self.seed)

    def create_network(self, config):
        # Create the network based on the config
        network = Network.initiate_network(config["network_size"]["x"], config["network_size"]["y"])
        return network

    def create_vehicles(self, config):
        # Create the vehicles based on the config
        vehicles = []
        for vehicle_config in config["vehicles"]:
            position = vehicle_config["position"]
            vehicle = Vehicle(vehicle_config["id"], position, vehicle_config["state"])
            vehicles.append(vehicle)
            cell = self.network.get_cell(position[0], position[1])
            if cell:
               cell.vehicle = vehicle
        return vehicles

    def update_state(self):
        # Update the state of the environment

        # Collect the number of vehicles in each state
        state_counts = {
            "Infected": 0,
            "Not infected": 0,
            "Repaired": 0,
            "Broken down": 0
        }

      
        for vehicle in self.vehicles:
            state = vehicle.get_state()
            state_counts[state] += 1

            # Get the current cell and its neighbors
            current_cell = self.network.get_cell(vehicle.x, vehicle.y)
            neighbors = self.network.get_cell(vehicle.x, vehicle.y).neighbors

            # Filter the neighboring cells to find valid move destinations and create the list according to their proability
            valid_destinations = []
            special_destinations = []
            probabilities = []
            choice = None
            for neighbor in neighbors:
               if neighbor.type == "Road" and neighbor.vehicle is None:
                  valid_destinations.append(neighbor)
               elif neighbor.vehicle is None:
                  special_destinations.append(neighbor)
                  probabilities.append(neighbor.probability)
            
            for i in range(len(probabilities)):
               if probabilities[i] > random.random():
                  choice = special_destinations[i]

            if not choice:
               choice = random.choice(valid_destinations)

                # Move the vehicle to the destination cell
               current_cell.vehicle = None
               choice.vehicle = vehicle
               vehicle.x, vehicle.y = choice.x, choice.y

        # Store the state counts for the current tick
        self.tick_stats["Infected"].append(state_counts["Infected"])
        self.tick_stats["Not infected"].append(state_counts["Not infected"])
        self.tick_stats["Repaired"].append(state_counts["Repaired"])
        self.tick_stats["Broken down"].append(state_counts["Broken down"])

        return state_counts