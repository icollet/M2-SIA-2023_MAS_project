import tkinter as tk
import random

from elements.Vehicle import Vehicle

class VehicleGridApp(tk.Frame):
    # Can't really go to more than 18
    def __init__(self, master, grid_size=15):
        super().__init__(master)
        self.grid_size = grid_size
        self.vehicles = []
        self.canvas = tk.Canvas(self, width=50 * grid_size, height=50 * grid_size)
        self.canvas.pack()
        self.master = master
        self._draw_grid()
        
    def _draw_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                self.canvas.create_rectangle(
                    50 * i, 50 * j, 50 * (i + 1), 50 * (j + 1), fill="white"
                )

    def update_vehicles(self, vehicles):
        self.vehicles = vehicles
        self.canvas.delete("vehicle")
        for vehicle in self.vehicles:
            if vehicle.state == "Not infected": color = "green"
            elif vehicle.state == "Infected": color = "red"
            elif vehicle.state == "Repaired": color = "blue"
            elif vehicle.state == "Broken down" : color = "black"
            i = vehicle.x
            j = vehicle.y
            self.canvas.create_oval(
                50 * i + 10, 50 * j + 10, 50 * (i + 1) - 10, 50 * (j + 1) - 10, 
                fill=color, tags="vehicle"
            )
            self.master.update()

