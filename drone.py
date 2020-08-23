from utils import Utils
from interval import Interval
class Drone:
    def __init__(self):
        self.inputFile = './inputPS6.txt'
        self.promptFile = './promptsPS6.txt'
        self.utils = Utils()
        self.intervals = None

    def readInputFromInputFile(self):
        lines = self.utils.readFromInputFile(self.inputFile)
        self.intervals = [Interval]*len(lines)
        for line in lines:
            data = line.strip('\n').strip().split('/')
            self.intervals[int(data[0]) - 1] = Interval(int(data[1]), int(data[2]))

        for interval in self.intervals:
            print(interval.manufacturingTime, interval.flightTestingTime)

if __name__ == '__main__':
    ob = Drone()
    ob.readInputFromInputFile()