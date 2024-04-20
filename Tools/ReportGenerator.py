class ReportGenerator:

    # Constructor for utilizing the package manager and address manager
    def __init__(self, package_manager, address_manager):
        self.package_manager = package_manager
        self.address_manager = address_manager

    # Method for generating a report on the total miles of x number of trucks
    def get_total_miles(self, *trucks):
        miles = 0.0
        for truck in trucks:
            miles+= truck.miles_driven
        print(f"The total miles traveled are {miles}")

    # Method for getting the status of a specific package at a specific time
    def get_package_status(self, ID, time):
        package = self.package_manager.get_package(ID)
        package.update_status(time)
        print(f"At {time}, the package was {package.status}.")
        print(f"The package delivery address is: {package.address}")
        print(f"Delivery time is {package.delivery_time}")


    # Method for getting a full report on packages at a specific time
    def full_report(self, time):
        packages = self.package_manager.packages
        #Report Header
        print(f"==== Full Package Report at Time: {time} ====")

        # Iterating through the packages in the hashtable and printing the report
        # Updating the status of the report based on the user's input
        for i in range(len(self.package_manager.packages)):
            package = self.package_manager.get_package(i + 1)
            package.update_status(time)
            print(f"ID: {package.ID}, Truck Number: {package.truck_number}, Deadline: {package.delivery_deadline},"
                  f"Status: {package.status}, Address: {package.address}, Notes: {package.notes}")
        #Report Footer
        print("==== End Report ====")
