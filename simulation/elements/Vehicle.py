class Vehicle:
    def __init__(self, vehicle_id, position, state):
        self.vehicle_id = vehicle_id
        self.x, self.y = position
        self.state = state

    def update_state(self, new_state):
        self.state = new_state

    def update_position(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def get_state(self):
        return self.state

    def get_position(self):
        return self.x, self.y