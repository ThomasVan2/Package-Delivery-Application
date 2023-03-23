# Truck class
class Truck:

    def __init__(self, maxNumberPackages, speed, departureTime, listPackages, mileage, load, totalTime, status,
                 end_time,points):
        self.maxNumberPackages = maxNumberPackages
        self.speed = speed
        self.departureTime = departureTime
        self.listPackages = listPackages
        self.mileage = mileage
        self.load = load
        self.totalTime = totalTime
        self.status = status
        self.end_time = end_time
        self.points = points

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (
        self.maxNumberPackages, self.speed, self.departureTime, self.listPackages, self.mileage, self.load,
        self.totalTime, self.status, self.end_time, self.points)

    def truck_status(self, time):
        if time < self.departureTime:
            self.status = "At the hub"
        elif self.departureTime < time < self.end_time:
            self.status = "en route"
        elif time > self.end_time:
            self.status = "Packages delivered: back at the hub"
