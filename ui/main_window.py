import tkinter as tk
import random

class VehicleGridApp(tk.Frame):
    def __init__(self, master, grid_size=10):
        super().__init__(master)
        self.grid_size = grid_size
        self.vehicle_states = {}
        self.canvas = tk.Canvas(self, width=500, height=500)
        self.canvas.pack()
        self._draw_grid()
        
    def _draw_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                self.canvas.create_rectangle(
                    50 * i, 50 * j, 50 * (i + 1), 50 * (j + 1), fill="white"
                )

    def update_vehicles(self, vehicle_states):
        self.vehicle_states = vehicle_states
        self.canvas.delete("vehicle")
        for (i, j), state in self.vehicle_states.items():
            color = "green" if state == "not_infected" else "red"
            self.canvas.create_oval(
                50 * i + 10, 50 * j + 10, 50 * (i + 1) - 10, 50 * (j + 1) - 10, 
                fill=color, tags="vehicle"
            )

def generate_vehicle_states(num_vehicles, infection_rate, grid_size):
    states = {}
    for _ in range(num_vehicles):
        x, y = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
        state = "infected" if random.random() < infection_rate else "not_infected"
        states[(x, y)] = state
    return states

def main():
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
        vehicle_states = generate_vehicle_states(num_vehicles, infection_rate, app.grid_size)
        app.update_vehicles(vehicle_states)

    start_button = tk.Button(root, text="Démarrer la Simulation", command=start_simulation)
    start_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
