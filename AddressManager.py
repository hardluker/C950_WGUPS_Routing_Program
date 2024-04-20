import csv

class AddressManager:

    #Constructor for initializing datasets into working memory during instantiation "Caching"
    def __init__(self, address_directory, distances_directory):
        self.addresses = self.load_addresses(address_directory)
        self.distances = self.load_distances(distances_directory)

    #Method for loading the Addresses Information
    def load_addresses(self, address_directory):
        with open(address_directory) as address_file:
            reader = csv.reader(address_file)
            addresses = list(reader)
        return addresses

    #Method for loading the adjacency matrix
    def load_distances(self, distances_directory):
        with open(distances_directory) as distance_file:
            reader = csv.reader(distance_file)
            distances = list(reader)
        return distances

    #Method for getting the address ids to utilize as axes in the adjacency matrix
    def get_address_id(self, street):
        for address in self.addresses:
            if street == address[2]:
                return int(address[0])

    #Method that gets axis information and reads the adjacency matrix for the distance between two addresses.
    def get_address_differences(self, street1, street2):
       x_axis = self.get_address_id(street1)
       y_axis = self.get_address_id(street2)

       distance = self.distances[x_axis][y_axis]
       if distance == '':
           distance = self.distances[y_axis][x_axis]
       return float(distance)
