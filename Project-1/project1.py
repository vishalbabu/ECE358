from numpy import random

from packet import packet
from departure import departure

# x is number of random vars to generate, in the form of a list
random.uniform(0.0, 1.0, x)


def main(args):
    intialize_variables(args)
    t_arrival = calc_arrival_time()  # calculate first packet arrival time
    pkt = packet.packet()
    for x in xrange(num_of_ticks):  # TODO: need to calculate this
        arrival()  # generate packet, load into queue
        retval = departure(x, pkt)  # pop off queue, process, continue
        if retval == 1:
            # also record x as departure time
            # and get the next packet
            pkt = queue.pop()

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
