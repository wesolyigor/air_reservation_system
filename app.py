from pprint import pprint as pp

class Flight:
    def __init__(self, flight_number, airplane):
        self.flight_number = flight_number
        self.airplane = airplane

        rows, seats = airplane.get_seating_plan()
        self.seats = [{seat: None for seat in seats} for row in rows]

    def get_airline(self):
        return self.flight_number[:2]

    def get_flight_number(self):
        return self.flight_number[2:]

    def get_plane(self):
        return self.airplane.get_name()

    def allocate_passengeer(self, passenger="Igor Wesołowski", seat="24A"):
        row, letter = self._parse_seat(seat)

    def _parse_seat(self, seat):
        rows, letters = self.airplane.get_seating_plan()

        letter = seat[-1]
        if letter not in letters:
            raise ValueError(f"Inwalid seat letter: {letter}")

        row_text = seat[:-1]

        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid seat number: {row_text}")

        if row not in rows:
            raise ValueError(f"Seat number is out of range: {row}")

        return row, letter

    def relocate_passenger(self, from_seat, to_seat):
        pass


class Plane:
    def get_num_seats(self):
        rows, seats = self.get_seating_plan()
        return len(rows) * len(seats)

class Airbus370(Plane):
    def get_name(self):
        return "Airbus A370"

    def get_seating_plan(self):
        return range(25), "ABCDEG"


class Boeing777(Plane):
    def get_name(self):
        return "Boeing777"

    def get_seating_plan(self):
        return range(40), "ABCDEGHIK"


f = Flight("LO123", Airbus370())
#print((airplane.get_num_seats()))
#print(airplane.get_name())
#print(f.get_plane())
#print(f.flight_number)
#print(f.get_airline())
# print(f.get_flight_number())
pp(f.seats)

