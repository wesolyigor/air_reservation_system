from pprint import pprint as pp
from flight import Flight
from Airplanes import *
from helpers import *




f = Flight("LO123", Airbus370())
f.allocate_passengeer(passenger="Lech K.", seat="10B")
f.allocate_passengeer(passenger="Jarosław K.", seat="10C")
f.allocate_passengeer(passenger="Igor W.", seat="10D")
f.relocate_passenger("10B", "20D")
print(f.num_empty_seats())
f.print_tickets(card_printer)


#print((airplane.get_num_seats()))
#print(airplane.get_name())
#print(f.get_plane())
#print(f.flight_number)
#print(f.get_airline())
# print(f.get_flight_number())
pp(f.seats)

