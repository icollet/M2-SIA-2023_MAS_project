from elements.Cell import Cell


class Network:
    def __init__(self, dims):
        self.cells = []
        self.matrix_state = None
        self.dims = dims

    def add_cell(self, cell):
        self.cells.append(cell)

    def connect_cells(self, cell1, cell2):
        cell1.add_neighbor(cell2)
        cell2.add_neighbor(cell1)

    def get_cell(self, x, y):
        for cell in self.cells:
            if cell.x == x and cell.y == y:
                return cell
        return None
    
    def print_cell_content(self):
        i = 0
        for cell in self.cells:
            if i % self.dims[0] == 0:
                print()
            i += 1
            vehicle = cell.vehicle
            if vehicle is None:
                print("x", end=" ")
            else:
                state = vehicle.get_state()
                if state == "Infected":
                    print("I", end=" ")
                elif state == "Not infected":
                    print("N", end=" ")
                elif state == "Repaired":
                    print("R", end=" ")
                elif state == "Broken down":
                    print("B", end=" ")
            
        print()

    @staticmethod
    def initiate_network(x, y):
        network = Network((x, y))

        for i in range(x):
            for j in range(y):
                # if special cell (schools, etc.), the proability should be higher
                cell = Cell(i, j, "Road", None, 0.25)
                network.add_cell(cell)
                
                if i > 0:
                    network.connect_cells(cell, network.cells[(i - 1) * y + j])
                if j > 0:
                    network.connect_cells(cell, network.cells[i * y + (j - 1)])

        return network
    



