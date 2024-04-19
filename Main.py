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


# Creating the HashTable and inserting the packages into it. The size is 52
# hash_table = HashTable(52)
# insert_packages_into_hash_table("CSV_Files/Packages.csv", hash_table)



# address2 = hash_table.get(2).address
# address1 = hash_table.get(30).address

# address_manager = AddressManager()

# difference = address_manager.get_address_differences(address1, address2)



# print(f"The distance between {address1} and {address2} is: {difference}")
# Instantiating and "Loading" the trucks with a list of the package IDs.
# truck1 = Truck(16, 0, [], 18, 0.0, )