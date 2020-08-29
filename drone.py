from utils import Utils
from interval import Interval


class Drone:
    def __init__(self):
        self.inputFile = './inputPS6.txt'
        self.outputFile = './outputPS6.txt'
        self.utils = Utils()
        self.intervals = None
        self.outputResultList = []

    def readInputFromInputFile(self):
        lines = self.utils.readFromInputFile(self.inputFile)
        self.intervals = [Interval] * len(lines)
        for line in lines:
            data = line.strip('\n').strip().split('/')
            # list index starts from 0
            self.intervals[int(data[0].strip()) - 1] = Interval(int(data[0].strip()), int(data[1].strip()),
                                                                int(data[2].strip()))

    def scheduleTask(self):
        """
        there is just one unit, so at a time only one drone can be manufactured and we have one unit for testing, so
        only one unit can be tested.
        :return:
        """
        # we need to schedule all the drone in minimum time
        # sorting based on increasing order of manufacturing Time
        scheduled_tasks = []  # list to represent all the scheduled task
        interval_list = list(self.intervals)
        interval_list.sort(
            key=lambda x: x.manufacturingTime)  # so that we know which drone will be manufactured first based on time

        id_list = []
        for interval in interval_list:
            id_list.append(str(interval.getId()))

        self.outputResultList.append("Drones should be produced in the order:" + ','.join(id_list))

        # now we need to schedule all the task and corresponding for the flight testing
        flight_testing_schedule = []
        last_flight_testing_time = None
        for interval in interval_list:
            # this is total time for manufacturing
            for time_unit in range(interval.getManufacturingTime()):
                scheduled_tasks.append(interval.getId())

            # now we need to schedule for flight testing
            if last_flight_testing_time is not None:
                while last_flight_testing_time <= interval.getManufacturingTime():
                    flight_testing_schedule.append('IDLE')
                    last_flight_testing_time += 1

            for time_unit in range(interval.getFlightTestingTime()):
                flight_testing_schedule.append(interval.getId())

            last_flight_testing_time = len(flight_testing_schedule)

        self.outputResultList.append(
            'Total production time for all drones is:' + str(max(len(flight_testing_schedule), len(scheduled_tasks))))
        idle_time_unit = lambda x: x == 'IDLE', flight_testing_schedule
        self.outputResultList.append('Idle time of flight testing unit:' + str(len(idle_time_unit)))
        self.utils.writeToOutputFile(self.outputFile, self.outputResultList)


if __name__ == '__main__':
    ob = Drone()
    ob.readInputFromInputFile()
    ob.scheduleTask()
