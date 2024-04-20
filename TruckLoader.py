from Truck import Truck
from PackageManager import PackageManager
import re
class TruckLoader:
    def __init__(self, package_manager):
        self.truck1 = Truck(1, [])
        self.truck2 = Truck(2, [])
        self.truck3 = Truck(3, [])
        self.trucks = [self.truck1, self.truck2, self.truck3]
        self.package_manager = package_manager
        self.id_queue = []
        self.loaded_ids = []


    # Method for "loading" the trucks with a specific package_id
    # If the ID is not in the queue, it will not be loaded
    def load_truck(self, truck_number, ID):
        if ID in self.id_queue:
            self.trucks[truck_number - 1].packages.append(ID)
            self.loaded_ids.append(ID)
        else:
            print(f"Package with ID: {ID}, is not in the queue")



    # Method for building a working queue for distributing packages
    def load_id_queue(self):
        for i in range(len(self.package_manager.packages)):
            package = self.package_manager.get_package(i+1)
            self.id_queue.append(package.ID)

    def clear_queues(self):
        for ID in self.loaded_ids:
            try:
                id_queue.remove(ID)
            except:
                print(f"Id is not in queue: {ID}")
        self.loaded_ids = []


    # Method for prioritizing packages based on delivery deadline
    def prioritize_packages(self):
        for ID in self.id_queue:
            package = self.package_manager.get_package(ID)
            if package.delivery_deadline == "10:30 AM":
                package.priority = 2

            if package.delivery_deadline == "9:00 AM":
                package.priority = 3

    # Method for distributing standard non-prioritized packages between trucks via round-robin
    def load_standard_packages(self):
        print(self.id_queue)
        truck_number = 1 # Variable for tracking round-robin index
        for ID in self.id_queue:
            package = self.package_manager.get_package(ID)
            if package.delivery_deadline.strip() == 'EOD' and package.notes.strip() == '':
                self.load_truck(truck_number, ID)
                # Circular distribution through the truck index
                truck_number = ((truck_number + 1) % len(self.trucks)) + 1
        self.clear_queues()


    # Method for distributing packages designated to specific trucks
    def load_truck_specific_packages(self):
        for ID in self.id_queue:
            package = self.package_manager.get_package(ID)
            if "Can only be on truck" in package.notes:
                truck_number = int(package.notes.split()[-1])
                self.load_truck(truck_number, ID)
        self.clear_queues()

    # Distributing packages that are dur at 9:00 AM into truck 1 (Priority Truck)
    def load_express_priority(self):
        for ID in self.id_queue:
            package = self.package_manager.get_package(ID)
            if package.priority == 3:
                self.load_truck(1, ID)
        self.clear_queues()

    # Determines if there are still packages associated with package sets in the queue
    def package_sets(self):
        for ID in self.id_queue:
            package = self.package_manager.get_package(ID)
            if "Must be delivered with" in package.notes:
                return True

    # This method distributes the package sets that are required to be together
    def load_package_sets(self):
        while self.package_sets():
            for ID in self.id_queue:
                package = self.package_manager.get_package(ID)
                if "Must be delivered with" in package.notes:
                    # Using RegEx to extract necessary package sets
                    package_numbers = re.findall(r'\b\d+\b', package.notes)

                    for number in package_numbers:
                        for truck in self.trucks:
                            if int(number) in truck.packages:
                                self.load_truck(truck.truck_number, ID)
            self.clear_queues()


    def load_delayed_packages(self):
        for ID in self.id_queue:
            package = self.package_manager.get_package(ID)
            if "will not arrive to depot until 9:05 am" in package.notes:
                if package.delivery_deadline == "EOD":
                    self.load_truck(2, ID)
                else:
                    self.load_truck(3, ID)
        self.clear_queues()