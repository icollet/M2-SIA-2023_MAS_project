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
        self.p_infected = config["probabilities"]["p_inf"]
        self.p_repaired = config["probabilities"]["p_rep"]
        self.p_break = config["probabilities"]["p_break"]

    def create_network(self, config):
        # Create the network based on the config
        network = Network.initiate_network(config["network_size"]["x"], 
                                            config["network_size"]["y"])
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

        # Vehicles movements
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
               if len(valid_destinations) > 0:
                choice = random.choice(valid_destinations)

                    # Move the vehicle to the destination cell
                current_cell.vehicle = None
                choice.vehicle = vehicle
                vehicle.x, vehicle.y = choice.x, choice.y

        # Format [(Vehicle, new_state)] so all the vehicles are updated together
        apply_list = []
        # Vehicles behaviours
        for vehicle in self.vehicles:
            state = vehicle.get_state()
            if state != "Broken down":
                state = vehicle.get_state()
                neighbouring_cells = self.network.get_cell(vehicle.x, vehicle.y).neighbors
                neighbouring_vehicles = []
                for cell in neighbouring_cells:
                    if cell.vehicle:
                        neighbouring_vehicles.append(vehicle)
                for n_vehicle in neighbouring_vehicles:
                    v_state = n_vehicle.get_state()
                    if state == "Not infected" or state == "Repaired":
                        if v_state == "Infected":
                            if random.random() <= self.p_infected:
                                apply_list.append((vehicle, "Infected"))
                if state == "Infected":
                    rest = 1 - (self.p_repaired + self.p_break)
                    results = ["Repaired"] * int(self.p_repaired * 100) + ["Broken down"] * int(self.p_break * 100) + ["Infected"] * int(rest * 100)
                    apply_list.append((vehicle, random.choice(results)))

        # Apply the new state
        for change in apply_list:
            change[0].update_state(change[1])

        # Store the state counts for the current tick
        self.tick_stats["Infected"].append(state_counts["Infected"])
        self.tick_stats["Not infected"].append(state_counts["Not infected"])
        self.tick_stats["Repaired"].append(state_counts["Repaired"])
        self.tick_stats["Broken down"].append(state_counts["Broken down"])

        return state_counts