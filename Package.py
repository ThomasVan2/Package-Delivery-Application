# Class for packages
class Package:
    def __init__(self, ID, address, city, state, zip, deadLine, weight, notes,status, delivery_time, enroute_time, pLatitude, pLongitude):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadLine = deadLine
        self.weight = weight
        self.notes = notes
        self.status = status
        self.delivery_time = delivery_time
        self.enroute_time = enroute_time
        self.pLatitude = pLatitude
        self.pLongitude = pLongitude

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (
        self.ID, self.address, self.city, self.state, self.zip, self.deadLine, self.weight, self.notes, self.status,
        self.delivery_time, self.pLatitude, self.pLongitude)

    def change_status(self, time, delivery_time):
        if self.enroute_time > time:
            self.status = "At the hub, projected time of deliver:"
        elif delivery_time <= time:
            self.status = "delivered at: "
        elif delivery_time > time:
            self.status = "en route, projected time of deliver:"
