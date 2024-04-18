class Truck:
    #Constructor
    def __init__(self, capacity, load_size, packages, speed, miles_driven, current_address, depart_time):
        self.capacity = capacity
        self.load_size = load_size
        self.packages = packages
        self.speed = speed
        self.miles_driven = miles_driven
        self.current_address = current_address
        self.depart_time = depart_time
        self.current_time = depart_time