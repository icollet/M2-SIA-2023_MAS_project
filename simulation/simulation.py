from elements.Cell import Cell
from elements.Network import Network
from elements.Vehicle import Vehicle
from elements.Environment import Environment


CONFIG = {
    "network_size": {"x": 4, "y": 3},
    "probabilities" : {"p_inf" : 0.2, "p_rep" : 0.2, "p_break" : 0.2},
    "vehicles": [
        {"id": 1, "position": (0, 0), "state": "Not infected"},
        {"id": 2, "position": (1, 2), "state": "Infected"},
        # ...
    ]
}


if __name__ == "__main__":
    env = Environment(CONFIG)
    network = env.network
    vehicles = env.vehicles

    for vehicle in vehicles:
        print(f"Vehicle ID: {vehicle.vehicle_id}")
        print(f"Position: {vehicle.get_position()}")
        print(f"State: {vehicle.get_state()}")
        print()
