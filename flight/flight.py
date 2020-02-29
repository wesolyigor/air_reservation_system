class Flight:
    def __init__(self, flight_number, airplane):
        self.flight_number = flight_number
        self.airplane = airplane

        rows, seats = airplane.get_seating_plan()
        self.seats = [None] + [{seat: None for seat in seats} for _ in rows]

    def get_airline(self):
        return self.flight_number[:2]

    def get_flight_number(self):
        return self.flight_number[2:]

    def get_plane(self):
        return self.airplane.get_name()

    def allocate_passengeer(self, passenger="Igor Wesołowski", seat="24A"):
        row, letter = self._parse_seat(seat)

        if self.seats[row][letter] is not None:
            raise ValueError(f"Seat is already taken{seat}")

        self.seats[row][letter] = passenger

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
        from_row, from_letter = self._parse_seat(from_seat)

        if self.seats[from_row][from_letter] is None:
            raise ValueError(f"No passenger to relocate {from_seat}")

        to_row, to_letter = self._parse_seat(to_seat)

        if self.seats[to_row][to_letter] is not None:
            raise ValueError(f"Seat is already taken {to_seat}")

        self.seats[to_row][to_letter] = self.seats[from_row][from_letter]
        self.seats[from_row][from_letter] = None

    def num_empty_seats(self):
        return sum(sum(1 for seat in row.values()
                       if seat is None)
                   for row in self.seats if row is not None)

    def print_tickets(self, c_printer):
        for passenger, seat in self.get_passenger_list():
            c_printer(passenger, seat, self.get_plane(), self.flight_number)


    def get_passenger_list(self):
        rows, letters = self.airplane.get_seating_plan()

        for row in rows:
            for letter in letters:
                passenger = self.seats[row][letter]
                if passenger is not None:
                    yield passenger, f"{row}{letter}"
