from math import *
import random


def read_cities(file_name):
    '''Read in the cities from the given file_name, and return them as a list of four-tuples:
       [(state, city, latitude, longitude), ...] Use this as your initial road_map, that is,
       the cycle Alabama → Alaska → Arizona → ... → Wyoming → Alabama.'''
    file = open(file_name,'r')
    road_map = []
    for line in file:
        road_map.append(tuple(line.strip().split('\t')))
    file.close()
    return road_map
    

def print_cities(road_map):
    '''Prints a list of cities, along with their locations. Print only one or two digits
       after the decimal point. '''
    print_map = []
    for element in road_map:
        print_map.append((element[1], (round(float(element[2]), 2), round(float(element[3]), 2))))
    print (print_map)


def distance(lat1degrees, long1degrees, lat2degrees, long2degrees):
    earth_radius = 3956  # miles
    lat1 = radians(lat1degrees)
    long1 = radians(long1degrees)
    lat2 = radians(lat2degrees)
    long2 = radians(long2degrees)
    lat_difference = lat2 - lat1
    long_difference = long2 - long1
    sin_half_lat = sin(lat_difference / 2)
    sin_half_long = sin(long_difference / 2)
    a = sin_half_lat ** 2 + cos(lat1) * cos(lat2) * sin_half_long ** 2
    c = 2 * atan2(sqrt(a), sqrt(1.0 - a))
    return earth_radius * c


def compute_total_distance(road_map):
    '''Returns, as a floating point number, the sum of the distances of all the connections
       in the road_map. Remember that it's a cycle, so that (for example) in the initial 
       road_map, Wyoming connects to Alabama.'''
    total_distance = 0.0
    r = road_map
    i = -1
    while i < len(r) - 1: 
        total_distance += distance(float(r[i][2]), float(r[i][3]), float(r[i + 1][2]), float(r[i + 1][3]))
        i += 1
    return total_distance


def swap_adjacent_cities(road_map, index):
    '''Take the city at location index in the road_map, and the city at location index+1
       (or at 0, if index refers to the last element in the list), swap their positions
       in the road_map, compute the new total distance, and return the tuple
       (new_road_map, new_total_distance).'''
    new_road_map = road_map[:]
    original_index = new_road_map[index]
    new_road_map[index] = new_road_map[(index + 1) % len(road_map)]
    new_road_map[(index + 1) % len(road_map)] = original_index
    new_total_distance = compute_total_distance(new_road_map)
    return ((new_road_map, new_total_distance))


def swap_cities(road_map, index1, index2):
    '''Take the city at location index in the road_map, and the city at location index2,
       swap their positions in the road_map, compute the new total distance, and return
       the tuple (new_road_map, new_total_distance). Allow the possibility that
       index1=index2, and handle this case correctly.'''
    new_road_map = road_map[:]
    if index1 != index2:
        original_index = new_road_map[index1]
        new_road_map[index1] = new_road_map[index2]
        new_road_map[index2] = original_index
    new_total_distance = compute_total_distance(new_road_map)
    return ((new_road_map, new_total_distance))


def find_best_cycle(road_map):
    '''Using a combination of swap_cities and swap_adjacent_cities, try 10000 swaps,
       and each time keep the best cycle found so far. After 10000 swaps, return the
       best cycle found so far.'''
    shortest_distance = None
    best_cycle = road_map[:]
    for n in range(0, 7000):
        index1 = random.randint(0, len(road_map) - 1)
        index2 = random.randint(0, len(road_map) - 1)
        (new_cycle1, distance1) = swap_cities(best_cycle, index1, index2)  
        if shortest_distance is None or distance1 < shortest_distance:
            shortest_distance = distance1
            best_cycle = new_cycle1
    for n in range(0, 3000):
        index = random.randint(0, len(road_map) - 1)
        (new_cycle2, distance2) = swap_adjacent_cities(best_cycle, index)
        if distance2 < shortest_distance:
            shortest_distance = distance2
            best_cycle = new_cycle2
    return best_cycle
            

def print_map(road_map):
    '''Prints, in an easily understandable format, the cities and their connections,
       along with the cost for each connection and the total cost.'''
    b = find_best_cycle(road_map)
    i = -1
    for i in range(-1, len(b) - 1):
        cost = round(distance(float(b[i][2]), float(b[i][3]), float(b[i + 1][2]), float(b[i + 1][3])), 2)
        print (b[i][1], "-->", b[i + 1][1], "", "cost =", cost)
        i += 1
    print ("total cost = ", round(compute_total_distance(b),2))
        

def main():
    road_map = read_cities("city_data.txt")
    print_cities(road_map)
    compute_total_distance(road_map)
    find_best_cycle(road_map)
    print_map(road_map)


if __name__ == "__main__":
    main()
