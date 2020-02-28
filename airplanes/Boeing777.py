from plane import Plane

class Boeing777(Plane):
    def get_name(self):
        return "Boeing 777"

    def get_seating_plan(self):
        return range(1, 40), "ABCDEGHIK"