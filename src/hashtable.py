# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''  
        if self.storage[self._hash_mod(key)] is None:
            self.storage[self._hash_mod(key)] = LinkedPair(key, value)
        else:
            node = self.storage[self._hash_mod(key)]
            while node:
                if node.key is key:
                    node.value = value
                    break
                elif node.next is None:
                    node.next = LinkedPair(key, value)
                    break
                else:
                    node  = node.next

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''

        ind = self._hash_mod(key)
        if not self.storage[ind]:
            print("Warning: the key is not found")
            return
        
        node = self.storage[ind]
        previous_node = None
        while node:
            if node.key == key:
                if previous_node:
                    previous_node.next = node.next
                    break
                else:
                    self.storage[ind] = node.next
                    break
            elif node.next:
                previous_node = node
                node = node.next
            else:
                print("Warning: the key is not found")
                return


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        
        if self.storage[self._hash_mod(key)] is None:
            return None
        else:
            node = self.storage[self._hash_mod(key)]
            while node:
                if node.key == key:
                    return node.value
                elif node.next is None:
                    return None
                else:
                    node = node.next 


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        temp_list = []
        for i in self.storage:
            node = i
            while node:
                temp_list.append([node.key, node.value])
                node = node.next
        self.capacity = 2*self.capacity
        self.storage = [None]*self.capacity
        for i in temp_list:
            self.insert(i[0], i[1])



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing 
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
