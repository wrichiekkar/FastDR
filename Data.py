import numpy as np
#import matplotlib.pyplot as plt
#from collections import deque, namedtuple
import googlemaps
import re

a = np.loadtxt('er_List_3.txt', dtype=str, delimiter=', ')
names = []
wait_times = []
h_names = []
h_wait = []
h_travel = []
index_array = []
h_list = []

for i in range(0, len(a)):
    names.append(a[i][0])

for j in range(0, len(a)):
    wait_times.append(float(a[j][1]))

def time_and_distance(start, finish):
    # Requires API key
    gmaps = googlemaps.Client(key='AIzaSyAgYvR_kr-SFcn0HYOIT9PuAAGziAq4VTo')

    # Requires cities name
    my_dist = gmaps.distance_matrix(start, finish)['rows'][0]['elements'][0]

    # Printing the result
    time = (my_dist.get('duration').get('text'))
    dist = (my_dist.get('distance').get('text'))

    if len(time) > 8:
        s1 = time[:5]
        s2 = time[7:]
        time = float(re.findall("\d+", s1)[0]) * 60 + float(re.findall("\d+", s2)[0])
    else:
        time = float(re.findall("\d+", time)[0])
    #
    if dist[1] == ',':
        dist = (re.findall("([0-9]+[,.]+[0-9]+)", dist)[0])
        dist = float(dist.replace(',', ''))
    else:
        dist = float(dist.split(' ')[0])

    #print(dist, 'km, ', time, 'mins')
    x = [time, dist]
    return x

def dist_from_current_location():
    radius = 60
    current = 'RBC WaterPark Place'

    for h in names:
        x = (time_and_distance(current, h)[1])
        y = (time_and_distance(current, h)[0])
        if x <= radius:
            h_travel.append(y)
            h_list.append(x)
            index_array.append(names.index(h))
    return(h_list)


h_total_time = []
sorted_name = []
sorted_travel_time = []
sorted_wait_time = []
sorted_total_time = []
def output():
    dist_from_current_location()
    k = 0
    for i in index_array:
        h_wait.append(wait_times[i]*60)
        h_names.append(names[i])
        h_total_time.append(wait_times[i]*60 + h_travel[k])
        k += 1

    h_dict = dict(zip(h_names, h_total_time))

    g = 1
    for key, value in sorted(h_dict.items(), key=lambda item: item[1]):
        #print("%s: %s" % (key, value))
        d = index_array.index(names.index(key))
        sorted_name.append(key)
        sorted_travel_time.append(int(h_travel[d]))
        sorted_wait_time.append(int(h_wait[d]))
        sorted_total_time.append(int(h_total_time[d]))
        g += 1
        if g == 21:
            break

    #print('\n', '------------------------------------------', '\n')
    #print(index_array[names.index('The Hospital For Sick Children')])
    print(sorted_name)
    print(sorted_travel_time)
    print(sorted_wait_time)
    print(sorted_total_time)
    #print(index_array)
    return

def call_to_data():
    output()

def name():
    return sorted_name
def travel():
    return sorted_travel_time
def wait():
    return sorted_wait_time
def total():
    return sorted_total_time

# use index 0 - 2 to access name, travel time, wait time and total time for top 3 choices.
#a = sorted_name[2]
#print(a)