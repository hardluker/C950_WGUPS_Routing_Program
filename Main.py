import csv
from HashTable import HashTable
from Package import Package


#Reading the Distances from the .csv
with open("distances.csv") as distance_file:
    reader = csv.reader(distance_file)
    distances = list(reader)

#Function for inserting the packages into the hash table
def insert_packages(file, HashTable):
    with open(file) as package_file:
        next(package_file) #Skipping the header in the csv file
        packages = csv.reader(package_file)
        for package in packages:
            package_id = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zip_code = package[4]
            delivery_deadline = package[5]
            weight = package[6]
            status = "In Hub"

            # Inputting the data into a package object
            package_to_insert = Package(package_id, address, city, state, zip_code,
                                        delivery_deadline, weight, status)
            HashTable.insert(package_id, package_to_insert)


hash_table = HashTable(30)

insert_packages("packages.csv", hash_table)


print(hash_table.get(7))