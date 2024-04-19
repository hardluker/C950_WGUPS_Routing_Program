from Truck import Truck
from PackageManager import PackageManager
class TruckLoader:
    def __init__(self, package_manager):
        self.truck1 = Truck([])
        self.truck2 = Truck([])
        self.truck3 = Truck([])
        self.package_manager = package_manager
        self.ready_to_be_loaded = []


    def prioritize_packages(self):
        for i in range(len(self.package_manager.packages)):
            package = self.package_manager.get_package(i+1)

            if package.delivery_deadline == "10:30 AM":
                package.priority = 2
            if package.delivery_deadline == "9:00 AM":
                package.priority = 3

    def load_standard_packages