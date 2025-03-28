from datetime import datetime
import pprint


def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v

pprint.pprint(flights)
print()

flights2 = {}
for k, v in flights.items():
    flights2[convert2ampm(k)] = v.title()

pprint.pprint(flights2)

# Usando for loops
flight_times = []
for ft in flights.keys():
    flight_times.append(convert2ampm(ft))

destinations = []
for dest in flights.values():
    destinations.append(dest.title())

pprint.pprint(flight_times)
pprint.pprint(destinations)

#
# Usando comprehensions
#
# 1. inicio con la  lista vacia
# ... comp_dest = []
#
# 2. le meto el for sin los ':'
# ... comp_dest = [for dest in flights.values()]
#
# 3. Hago el append de los datos que quiero sin poner 'append'
# ... comp_dest = [dest.title() for dest in flights.values()]
#

comp_ft = [convert2ampm(ft) for ft in flights.keys()]
comp_dest = [dest.title() for dest in flights.values()]

pprint.pprint(comp_ft)
pprint.pprint(comp_dest)
