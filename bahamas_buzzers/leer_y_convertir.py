from datetime import datetime
import pprint


def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


# # Read as CSV file into a collection of lists
# import csv
# with open('buzzers.csv') as data:
# for line in csv.reader(data):
#     print(line)

# # Read as CSV file into a collection of Dictionaries, keys in first line
# import csv
# with open('buzzers.csv') as data:
# for line in csv.DictReader(data):
#     print(line)

# Read as text into a dictionary
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

# Usando for loops para agregar las claves del diccionario a una lista
flight_times = []
for ft in flights.keys():
    flight_times.append(convert2ampm(ft))

destinations = []
for dest in flights.values():
    destinations.append(dest.title())

pprint.pprint(flight_times)
pprint.pprint(destinations)
print()

#
# Usando List Comprehensions
#
# 1. inicio con la  lista vacia
# ... comp_dest = []
#                 ==
#
# 2. le meto el for sin los ':'
# ... comp_dest = [for dest in flights.values()]
#                  ============================
#
# 3. Hago el append de los datos que quiero sin poner 'append'
# ... comp_dest = [dest.title() for dest in flights.values()]
#                  ============
#

comp_ft = [convert2ampm(ft) for ft in flights.keys()]
comp_dest = [dest.title() for dest in flights.values()]

pprint.pprint(comp_ft)
pprint.pprint(comp_dest)
print()

#
#  Vamos a transformar lo de antes en un dictionary comprehension
#
# flights2 = {}
# for k, v in flights.items():
#     flights2[convert2ampm(k)] = v.title()
#
# El signo igual '=' se convierte en dos puntos ':'
#
more_flights = {convert2ampm(k): v.title() for k, v in flights.items()}

print('More flights:')
pprint.pprint(flights2)
pprint.pprint(more_flights)
print()

#
# Filtrando comprehensions
#
# P.e.: solo los de freeport
# just_freeport = {}
# for k, v in flights.items():
#     if v == 'FREEPORT':
#         just_freeport[convert2ampm(k)] = v.title()
#
# 4. Añado la condición al final sin lod ':'
# ... just_freeport = {convert2ampm(k): v.title() for k, v in flights.items() if v == 'FREEPORT'}
#                                                                             ==================
# just_freeport = {convert2ampm(k): v.title()
#                  for k, v in flights.items()
#                  if v == 'FREEPORT'}

#
# Tres ejercicios
#
data = [1, 2, 3, 4, 5, 6, 7, 8]
evens = []
for num in data:
    if not num % 2:
        evens.append(num)

comp_evens = [num for num in data if not num % 2]

pprint.pprint(evens)
pprint.pprint(comp_evens)
print()

data = [1, 'one', 2, 'two', 3, 'three', 4, 'four']
words = []
for num in data:
    if isinstance(num, str):
        words.append(num)

comp_words = [num for num in data if isinstance(num, str)]

pprint.pprint(words)
pprint.pprint(comp_words)
print()

data = list('So long and thanks for all the fish'.split())
title = []
for word in data:
    title.append(word.title())

comp_title = [word.title() for word in data]

pprint.pprint(title)
pprint.pprint(comp_title)
print()

#
# Usando more_flights sacar:
# {'Freeport': ['09:35AM', '05:00PM'],
#  'Rock Sound': ['11:45AM', '05:55PM'],
#  'Treasure Cay': ['10:45AM', '12:00PM'],
#  'West End': ['09:55AM', '07:00PM']}
#
when = {}
for dest in set(more_flights.values()):
    print(f'{dest:15} --> {[k for k, v in more_flights.items() if v == dest]}')
    when[dest] = [k for k, v in more_flights.items() if v == dest]

pprint.pprint(when)

when2 = {dest: [k for k, v in more_flights.items() if v == dest]
         for dest in set(more_flights.values())}

pprint.pprint(when2)
