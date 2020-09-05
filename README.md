# Drone-Production


Steps we followed to make it work:

we need to first manufacture and then only it can go for flight testing.
 hence, we sorted all the intervals based on manufacturing time which took O(nlogn) of time for sorting.
 Now, we know which task we need to pick first.
 Next, we need to schedule flight testing once manufacturing is completed.
 But we need to keep in mind if there is a gap in manufacturing time and last flight testing, then the flight testing scheduler is in IDLE state, which we need to count.
 Hence we run a loop to check if the current manufacturing time is more than or equal to the last flight testing and if we put IDLE state in the flight Testing schedule.
 so we need O(n) for running for all the intervals of time
 Total complexity of the code is O(n) + O(nlogn) which is O(nlogn)


Class used for making it work:

class Interval:
  it's a POJO class for interval where we have id, flight testing time and manufacturing time
  
class Drone:
 it's the main class which does everything for scheduling the task, we have a method which takes the input and prepares the interval list.
