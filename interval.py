class Interval:

    def __init__(self, id, manufacturingTime, flightTestingTime):
        self.id = id
        self.manufacturingTime = manufacturingTime
        self.flightTestingTime = flightTestingTime

    def getManufacturingTime(self):
        return self.manufacturingTime

    def getFlightTestingTime(self):
        return self.flightTestingTime

    def getId(self):
        return self.id
