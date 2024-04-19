from PackageManager import PackageManager
from AddressManager import AddressManager
from Truck import Truck

# Instantiating PackageManager, providing packages directory
# This object utilizes the hashtable datastructure and provides an interface
package_manager = PackageManager("CSV_Files/Packages.csv")

# Instantiating AddressManager, Providing needed directories
# This object serves as an abstraction to useful address information processing
address_manager = AddressManager("CSV_Files/Addresses.csv", "CSV_Files/Distances.csv")

address1 = package_manager.get_package(1).address
address2 = package_manager.get_package(3).address

print(address_manager.get_address_differences(address1, address2))

