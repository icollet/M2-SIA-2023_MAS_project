from elements.Cell import Cell
from elements.Network import Network
from elements.Vehicle import Vehicle


class Environment:
    def __init__(self, config):
        self.network = self.create_network(config)
        self.vehicles = self.create_vehicles(config)
        self.tick_stats = {"Infected": [], "Not infected": [], "Repaired": [], "Broken down": []}

    def create_network(self, config):
        # Create the network based on the config
        network = Network.initiate_network(config["network_size"]["x"], config["network_size"]["y"])
        return network

    def create_vehicles(self, config):
        # Create the vehicles based on the config
        vehicles = []
        for vehicle_config in config["vehicles"]:
            vehicle = Vehicle(vehicle_config["id"], vehicle_config["position"], vehicle_config["state"])
            vehicles.append(vehicle)
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
        
        # Store the state counts for the current tick
        self.tick_stats["Infected"].append(state_counts["Infected"])
        self.tick_stats["Not infected"].append(state_counts["Not infected"])
        self.tick_stats["Repaired"].append(state_counts["Repaired"])
        self.tick_stats["Broken down"].append(state_counts["Broken down"])
        
        # Perform other state update logic as needed

        # Return the state counts for the current tick
        return state_counts