import datetime


class DispatchManager:
    # Standard Contructor for utilizing the PackageManager and the AddressManager
    def __init__(self, package_manager, address_manager):
        self.package_manager = package_manager
        self.address_manager = address_manager

    # Method for setting priority flag levels on packages based on delivery deadline
    def prioritize_packages(self, package_ids):
        for ID in package_ids:
            package = self.package_manager.get_package(ID)
            if package.delivery_deadline == "10:30 AM":
                package.priority = 2

            elif package.delivery_deadline == "9:00 AM":
                package.priority = 3

    # This method is for assigning a package to a specific truck
    def assign_to_truck(self, package_ids, truck):
        for ID in package_ids:
            package = self.package_manager.get_package(ID)
            package.truck_number = truck.truck_number

    # Utilizing nearest neighbor algorithm while updating truck time and package delivery information
    # This method simulates the delivery
    def simulate_delivery(self, package_list, truck):
        # while the list is not empty
        while len(package_list) > 0:
            # Resetting these values every iteration
            distance_from_next = 9999
            next_package = None

            # Nearest neighbor finding the absolute closest address from the truck
            # Utilizing address manager for address distances
            for package in package_list:
                if self.address_manager.get_address_differences(truck.current_address, package.address) <= distance_from_next:
                    distance_from_next = self.address_manager.get_address_differences(truck.current_address, package.address)
                    next_package = package

            # Append the closest address to the truck list
            truck.packages.append(next_package.ID)
            # Remove the package from the input list
            package_list.remove(next_package)
            # Setting trucks current address to the package address
            truck.current_address = next_package.address
            # Adding the miles to the truck driven
            truck.miles_driven += distance_from_next
            # Adding to the total time the truck has driven based on speed of truck
            truck.total_time += datetime.timedelta(hours=distance_from_next / truck.speed)
            #Updating the departure time and the delivery time for the package delivered
            next_package.departure_time = truck.depart_time
            next_package.delivery_time = truck.total_time



    # Ties everything together, sorts packages by priority, sends the trucks through the simulation
    def dispatch(self, truck):
        #Flagging the package priorities
        self.prioritize_packages(truck.packages)

        # Assigning the packages to the truck
        self.assign_to_truck(truck.packages, truck)


        # Lists for containing different tier package priorities
        standard_priority_packages = []
        express_priority_packages = []
        high_priority_packages = []

        # Adding the packages to the lists, temporarily clearing truck list
        for ID in truck.packages:
            package = self.package_manager.get_package(ID)
            if package.priority == 1:
                standard_priority_packages.append(package)
            elif package.priority == 2:
                express_priority_packages.append(package)
            elif package.priority == 3:
                high_priority_packages.append(package)
        truck.packages.clear()

        # High Priority packages get delivered first
        self.simulate_delivery(high_priority_packages, truck)
        #Express Priority packages get delivered next
        self.simulate_delivery(express_priority_packages, truck)
        #Standard priority packages get delivered last
        self.simulate_delivery(standard_priority_packages, truck)



