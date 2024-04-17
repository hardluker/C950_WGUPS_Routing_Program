import csv
import HashTable

#Reading the Packages from the .csv
with open("packages.csv") as package_file:
    reader = csv.reader(package_file)

#Reading the Distances from the .csv
with open("distances.csv") as package_file:
    reader = csv.reader(package_file)


hash_table = HashTable.HashTable(10)
hash_table.insert(10, 'apple')

print(hash_table.get(10))