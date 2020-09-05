class Interval:
    """
    This is the plane class which we have created for interval
    it has 3 fields
    id manufacture time and flight testing time
    """

    def __init__(self, id, manufacturingTime, flightTestingTime):
        self.id = id
        self.manufacturingTime = manufacturingTime
        self.flightTestingTime = flightTestingTime

    """
    this returns the manufacture time
    """
    def getManufacturingTime(self):
        return self.manufacturingTime

    """
    this returns the flight testing time
    """
    def getFlightTestingTime(self):
        return self.flightTestingTime

    """
    this returns the id of the interval
    """
    def getId(self):
        return self.id
