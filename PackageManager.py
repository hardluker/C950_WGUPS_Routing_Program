import csv
import math
from HashTable import HashTable
from Package import Package
class PackageManager:

    #Package Manager Constructor
    #Reads the packages as a list, calculates a table size 1.3x the list.
    #Then, creates hashtable and inserts them into the list
    def __init__(self, package_directory):
        self.packages = self.read_packages(package_directory)
        table_size = int(math.ceil(len(self.packages) * 1.3))
        self.hash_table = HashTable(table_size)
        self.insert_packages_into_hash_table(self.packages, self.hash_table)

    def read_packages(self, package_directory):
        with open(package_directory) as package_file:
            next(package_file)  # Skipping the header in the csv file
            return list(csv.reader(package_file))

    def insert_packages_into_hash_table(self, packages, hash_table):
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
            hash_table.insert(package_id, package_to_insert)

    def get_package(self, package_id):
        return self.hash_table.get(package_id)