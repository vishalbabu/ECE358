def departure(x):

    if t >= t_departure:
        queue.pop()

for i in rangex(TICKS):


# for (i = 1; i <= TICKS; i++) {
# /* TICKS is an integer constant that represents the duration of simulation */
# /* The time duration for which you want to simulate a system = TICKS * tick_duration
#  where tick_duration has been explained in the Discrete Time paragraph.
#  Choose those two constants depending upon your need. */
# /* This for() loop essentially implements the time axis with all those ticks in Fig. 2. */
# /* Now you can do whatever you want to do in the i-th tick:
#  Call the data packet generator to try to generate a new data packet.
#  Call the server to let it know that another tick has elapsed, and the sever will
#  decide if servicing the current data packet will end in this tick, thereby pushing the
#  data packet out of the queue.
# */
# } // Essentially, this loop drives all other modules in your simulator
# /* Now compute the various performance metrics using data that you have stored while executing
#  the for() loop. */
# // NOTE: Repeat the for() loop 5-10 times to compute average values…. One run of the for() loop with, say,
# TICKS = 100000 is not enough.