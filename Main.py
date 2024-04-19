import csv
from HashTable import HashTable
from Package import Package
from Truck import Truck

#Function for inserting the packages into the hash table
def insert_packages_into_hash_table(file, HashTable):
    with open(file) as package_file:
        next(package_file) #Skipping the header in the csv file
        packages = csv.reader(package_file)

        #Iterating through the items in the csv and defining them
        for package in packages:
            id = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zip_code = package[4]
            delivery_deadline = package[5]
            weight = package[6]
            status = "In Hub"

            # Inputting the data into a package object
            package_to_insert = Package(id, address, city, state, zip_code,
                                        delivery_deadline, weight, status)
            HashTable.insert(id, package_to_insert)


#Creating the HashTable and inserting the packages into it.
hash_table = HashTable(30)
insert_packages_into_hash_table("CSV_Files/Packages.csv", hash_table)


#Reading the Distances from the .csv
with open("CSV_Files/Distances.csv") as distance_file:
    reader = csv.reader(distance_file)
    distances = list(reader)

print(hash_table.get(7).address)
#Instantiating and "Loading" the trucks with a list of the package IDs.
#truck1 = Truck(16, 0, [], 18, 0.0, )