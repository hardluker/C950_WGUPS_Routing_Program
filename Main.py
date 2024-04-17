import csv

#Reading the Packages from the .csv
with open("packages.csv") as package_file:
    reader = csv.reader(package_file)
    print(list(reader))

#Reading the Distances from the .csv
with open("distances.csv") as package_file:
    reader = csv.reader(package_file)
    print(list(reader))