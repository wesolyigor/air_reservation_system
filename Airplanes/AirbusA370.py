from plane import Plane


class Airbus370(Plane):
    def get_name(self):
        return "Airbus A370"

    def get_seating_plan(self):
        return range(1, 25), "ABCDEG"
