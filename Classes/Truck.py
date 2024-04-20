class Truck:
    #Constructor
    def __init__(self, truck_number, capacity, packages, speed, miles_driven, current_address, depart_time):
        self.truck_number = truck_number
        self.capacity = capacity
        self.packages = packages
        self.current_quantity = len(packages)
        self.speed = speed
        self.miles_driven = miles_driven
        self.current_address = current_address
        self.depart_time = depart_time
        self.total_time = depart_time

    #Method for converting truck to string
    def __str__(self):
        return (f"Capacity: {self.capacity}, Current Quantity: {self.current_quantity},"
                f" Speed: {self.speed}, Miles Driven: {self.miles_driven}, Current Address: {self.current_address},"
                f" Departure Time: {self.depart_time}, Total Time: {self.total_time}")