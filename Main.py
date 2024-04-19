import csv
from HashTable import HashTable
from PackageManager import PackageManager
from AddressManager import AddressManager
from Truck import Truck

package_manager = PackageManager("CSV_Files/Packages.csv")

print(package_manager.get_package(1).address)


#Creating the HashTable and inserting the packages into it. The size is 52
#hash_table = HashTable(52)
#insert_packages_into_hash_table("CSV_Files/Packages.csv", hash_table)



#address2 = hash_table.get(2).address
#address1 = hash_table.get(30).address

#address_manager = AddressManager()

#difference = address_manager.get_address_differences(address1, address2)



#print(f"The distance between {address1} and {address2} is: {difference}")
#Instantiating and "Loading" the trucks with a list of the package IDs.
#truck1 = Truck(16, 0, [], 18, 0.0, )