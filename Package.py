# Class for Packages
class Package:


    #Constructor initializing variables
    def __init__(self, ID, address, city, state, zip, delivery_deadline, weight, status, priority):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.status = status
        self.priority = priority


    #Method for converting object to string
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zip,
                                                       self.delivery_deadline, self.weight,
                                                       self.status, self.priority)