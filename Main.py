# Name: Donald Azevedo
# Student ID: 011371173
# Class: C950 Data Structures and Algorithms II

import datetime

from PackageManager import PackageManager
from AddressManager import AddressManager
from DispatchManager import DispatchManager

from Truck import Truck

# Instantiating PackageManager, providing packages directory
# This object utilizes the hashtable data structure and provides an interface
package_manager = PackageManager("CSV_Files/Packages.csv")


# Instantiating AddressManager, Providing needed directories
# This object serves as an abstraction to useful address information processing
address_manager = AddressManager("CSV_Files/Addresses.csv", "CSV_Files/Distances.csv")


# Instantiating DispatchManager
# It utilizes AddressManager and PackageManager for dispatching trucks
dispatch_manager = DispatchManager(package_manager, address_manager)


# Manually "Loading" the trucks with packages via class constructor instantiation:

# Truck 1 (High Priority truck)
truck1 = Truck(16, [1, 13, 14, 15, 19, 16, 20, 29, 30, 31, 34, 37, 40], 18, 0.0,
               "4001 South 700 East", datetime.timedelta(hours=8))

# Truck 2 (Standard Priority truck)
truck2 = Truck(16, [3, 9, 17, 18, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 18, 0.0,
               "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))

# Truck 3 (Express Priority Truck)
truck3 = Truck(16, [2, 4, 5, 6, 7, 8, 12, 10, 11, 25, 28, 32, 33], 18, 0.0,
               "4001 South 700 East", datetime.timedelta(hours=9, minutes=5))

dispatch_manager.dispatch(truck1)

dispatch_manager.dispatch(truck3)

# Updating the package address for dispatch at 10:20 am
package_manager.update_address(9, "410 S State St")
dispatch_manager.dispatch(truck2)

print(truck1)
package1 = package_manager.get_package(6)
package2 = package_manager.get_package(25)


print(f"ID: {package1.ID}, Delivery Address: {package1.address}, Deadline: {package1.delivery_deadline} "
      f"Departure Time: {package1.departure_time}, Delivery time: {package1.delivery_time} ")
#print(truck3.packages)
#print(address_manager.get_address_differences(package1.address, package2.address))



