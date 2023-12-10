from elements.Cell import Cell


class Network:
    def __init__(self):
        self.cells = []

    def add_cell(self, cell):
        self.cells.append(cell)

    def connect_cells(self, cell1, cell2):
        cell1.add_neighbor(cell2)
        cell2.add_neighbor(cell1)

    @staticmethod
    def initiate_network(x, y):
        network = Network()

        for i in range(x):
            for j in range(y):
                cell = Cell(i, j)
                network.add_cell(cell)

                if i > 0:
                    network.connect_cells(cell, network.cells[(i - 1) * y + j])
                if j > 0:
                    network.connect_cells(cell, network.cells[i * y + (j - 1)])

        return network