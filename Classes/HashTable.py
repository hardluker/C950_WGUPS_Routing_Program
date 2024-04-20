class HashTable:

    # Create empty bucket list of given size
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    # Method for creating the two-dimensional list of "buckets"
    def create_buckets(self):
        return [[] for _ in range(self.size)]

    # Insert values into hash map
    def insert(self, key, val):

        # Hashing the key modulo of the size to store in the specific bucket
        hashed_key = hash(key) % self.size

        # Defining the bucket per the key generated
        bucket = self.hash_table[hashed_key]

        # Initializing key found as false
        key_found = False

        # Iterating over the bucket defining the index of the buckets and the records within
        for index, record in enumerate(bucket):
            # Tuple unpacking the record
            record_key, record_val = record

            # check if the bucket has same key as
            # the key to be inserted
            if record_key == key:
                key_found = True
                break

        # If the key is the same, overwrite it.
        # Otherwise, append it within the bucket.
        # This is chaining and is a solution for collisions
        if key_found:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))

    # Return searched value with specific key
    def look_up(self, key):

        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            # check if the bucket has same key as
            # the key being searched
            if record_key == key:
                found_key = True
                break

        # If the bucket has same key as the key being searched,
        # Return the value found
        # Otherwise indicate there was no record found
        if found_key:
            return record_val
        else:
            return "No record found"

    # Remove a value with specific key
    def delete(self, key):

        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            # check if the bucket has same key as
            # the key to be deleted
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return

    # To print the items of hash map
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)
