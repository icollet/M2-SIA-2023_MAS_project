from elements.Cell import Cell
from elements.Network import Network
from elements.Vehicle import Vehicle
from elements.Environment import Environment


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

    for tick in range(CONFIG["total_ticks"]):
        state_counts = environment.update_state()
        # Access the state counts for the current tick
        print(f"Tick {tick}: {state_counts}")
        # ...


