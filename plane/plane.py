class Plane:
    def get_num_seats(self):
        rows, seats = self.get_seating_plan()
        return len(rows) * len(seats)
