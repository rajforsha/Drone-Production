from utils import Utils
from interval import Interval
import sys


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
            self.intervals[int(data[0].strip()) - 1] = Interval(int(data[0].strip()), int(data[1].strip()), int(data[2].strip()))

        self.outputResultList.append("initial data:")
        self.outputResultList.append("Id    manufacturing time      flight testing time")
        for interval in self.intervals:
            self.outputResultList.append(str(interval.getId()) + '\t' + str(interval.getManufacturingTime()) + '\t' + str(
                interval.getFlightTestingTime()))

    def scheduleTask(self):
        """
        there is just one unit, so at a time only one drone can be manufactured and we have one unit for testing, so
        only one unit can be tested.
        :return:
        """
        # we need to schedule all the drone in minimum time
        # sorting based on manufacturing Time
        scheduled_tasks = []  # list to represent all the scheduled task
        interval_list = list(self.intervals)
        interval_list.sort(key=lambda x: x.manufacturingTime)  # so that we know which drone will be manufactured first
        self.outputResultList.append("sorted data")
        self.outputResultList.append("Id    manufacturing time      flight testing time")
        for interval in interval_list:
            self.outputResultList.append(
                str(interval.getId()) + '\t' + str(interval.getManufacturingTime()) + '\t' + str(interval.getFlightTestingTime()))

        id_list = []
        for interval in interval_list:
            id_list.append(str(interval.getId()))

        self.outputResultList.append("Drones should be produced in the order:"+ ','.join(id_list))
        last = -sys.maxsize
        for interval in interval_list:
            if last > 0:
                for i in range(interval.getManufacturingTime() - last):
                    scheduled_tasks.append('IDLE')

            for time_unit in range(interval.getManufacturingTime()):
                scheduled_tasks.append(interval.getId())

            last = interval.getFlightTestingTime()

        self.outputResultList.append(str(scheduled_tasks))
        self.outputResultList.append(str(len(scheduled_tasks)))
        self.utils.writeToOutputFile(self.outputFile, self.outputResultList)


if __name__ == '__main__':
    ob = Drone()
    ob.readInputFromInputFile()
    ob.scheduleTask()
