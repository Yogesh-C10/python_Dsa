class HashTable:
    def __init__(self, size=10):
        # Initialize the hash table with the given size
        self.size = size
        self.table = [None] * self.size

    # Hash function to map keys to table indices
    def _hash(self, key):
        return hash(key) % self.size

    # Insert a key-value pair into the hash table
    def insert(self, key, value):
        index = self._hash(key)
        original_index = index
        # Linear probing: Find the next available spot
        while self.table[index] is not None:
            if self.table[index][0] == key:  # Update the value if key is already present
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size  # Move to the next index
            if index == original_index:  # Table is full
                raise Exception("HashTable is full")
        # Insert the key-value pair at the available index
        self.table[index] = (key, value)

    # Retrieve a value by key from the hash table
    def get(self, key):
        index = self._hash(key)
        original_index = index
        # Linear probing: Look for the key
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size  # Move to the next index
            if index == original_index:  # We've checked the entire table
                break
        raise KeyError(f"Key {key} not found")

    # Remove a key-value pair from the hash table
    def remove(self, key):
        index = self._hash(key)
        original_index = index
        # Linear probing: Look for the key to remove
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None  # Remove the key-value pair
                # Rehash subsequent elements to fill the gap
                next_index = (index + 1) % self.size
                while self.table[next_index] is not None:
                    rehash_key, rehash_value = self.table[next_index]
                    self.table[next_index] = None
                    self.insert(rehash_key, rehash_value)  # Re-insert the item
                    next_index = (next_index + 1) % self.size
                return
            index = (index + 1) % self.size  # Move to the next index
            if index == original_index:  # We've checked the entire table
                break
        raise KeyError(f"Key {key} not found")

    # Display the hash table (for debugging purposes)
    def display(self):
        for i, item in enumerate(self.table):
            if item is not None:
                print(f"Index {i}: {item[0]} -> {item[1]}")
            else:
                print(f"Index {i}: Empty")


# Example usage:
hash_table = HashTable()

# Inserting key-value pairs
hash_table.insert("apple", 10)
hash_table.insert("banana", 20)
hash_table.insert("orange", 30)

# Displaying the hash table
hash_table.display()

# Retrieving a value by key
print("\nValue for 'banana':", hash_table.get("banana"))

# Removing a key-value pair
hash_table.remove("banana")
print("\nAfter removing 'banana':")
hash_table.display()

# Trying to retrieve a removed key (will raise KeyError)
try:
    print(hash_table.get("banana"))
except KeyError as e:
    print("\nError:", e)
