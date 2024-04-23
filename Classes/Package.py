# Class for Packages
class Package:


    #Constructor initializing variables
    def __init__(self, ID, address, city, state, zip, delivery_deadline, weight, status, priority, notes):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.status = status
        self.priority = priority
        self.notes = notes
        self.departure_time = None
        self.delivery_time = None
        self.truck_number = None

    # Method for defining status based on time input.
    def update_status(self, time):
        if self.delivery_time < time:
            self.status = "Delivered"
        elif self.departure_time < time:
            self.status = "Out for Delivery"
        else:
            self.status = "In Hub"



    # Method for converting object to string
    def __str__(self):
        return f"Package ID: {self.ID}, Address: {self.address}, City: {self.city}, State: {self.state}, ZIP: {self.zip}, " \
               f"Delivery Deadline: {self.delivery_deadline}, Weight: {self.weight}, Status: {self.status}, Priority: {self.priority}"

