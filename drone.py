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
            self.intervals[int(data[0]) - 1] = Interval(int(data[0]), int(data[1]), int(data[2]))

        self.outputResultList.append("initial data:")
        self.outputResultList.append("Id    manufacturing time      flight testing time")
        for interval in self.intervals:
            self.outputResultList.append(str(interval.getId()) + '\t' + str(interval.getManufacturingTime()) + '\t' + str(
                interval.getFlightTestingTime()))

    def scheduleTask(self):
        # we need to schedule all the drone in minimum time
        # sorting based on flight testing time
        scheduled_tasks = []  # list to represent all the scheduled task
        interval_list = list(self.intervals)
        interval_list.sort(key=lambda x: x.manufacturingTime)  # so that we know which drone will be manufactured first
        self.outputResultList.append("sorted data")
        self.outputResultList.append("Id    manufacturing time      flight testing time")
        for interval in interval_list:
            self.outputResultList.append(
                str(interval.getId()) + '\t' + str(interval.getManufacturingTime()) + '\t' + str(interval.getFlightTestingTime()))

        last = -sys.maxsize
        for interval in interval_list:
            if last > 0:
                for i in range(interval.getManufacturingTime() - last):
                    scheduled_tasks.append('IDLE')

            for time_unit in range(interval.getManufacturingTime()):
                scheduled_tasks.append(interval.getId())

            last = max(interval.getFlightTestingTime(), len(scheduled_tasks))

        self.outputResultList.append(str(scheduled_tasks))
        self.outputResultList.append(str(len(scheduled_tasks)))
        self.utils.writeToOutputFile(self.outputFile, self.outputResultList)


if __name__ == '__main__':
    ob = Drone()
    ob.readInputFromInputFile()
    ob.scheduleTask()
