<<<<<<< Updated upstream
from numpy import random

from packet import packet

# x is number of random vars to generate, in the form of a list
random.uniform(0.0, 1.0, x)

def main(args):
    intialize_variables(args)
    t_arrival = calc_arrival_time()  # calculate first packet arrival time
    for _ in num_of_ticks:
        arrival()
        departure()
    create_report()


def calc_arrival_time():
    u = rand(0, 1)  # generate random number between 0...1
    arrival_time = ((-1 / lambda) * log(1 - u) * 1000000)
    return arrival_time


def arrival():
    if t >= packet_arrival_time:
        packet_queue.add(new_packet)
        t_arrival = t + calc_arrival_time()
        t_departure = t + (packet_size / transmission_rate)
        # Also need to consider packet loss case when queue is full


def departure():
    if t >= t_departure:
        queue.pop()
=======

