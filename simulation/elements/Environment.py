from elements.Cell import Cell
from elements.Network import Network
from elements.Vehicle import Vehicle


class Environment:
    def __init__(self, config):
        self.network = self.create_network(config)
        self.vehicles = self.create_vehicles(config)

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