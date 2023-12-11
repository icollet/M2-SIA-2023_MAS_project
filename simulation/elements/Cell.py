from elements.Vehicle import Vehicle

class Cell:
    def __init__(self, x, y, type, vehicle, attractivity):
        self.x = x
        self.y = y
        self.neighbors = []
        self.type = type
        self.vehicle = vehicle
        self.probability = attractivity

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)