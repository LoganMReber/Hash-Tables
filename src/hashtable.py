# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        return hash(key)

    def _hash_mod(self, key):
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash_mod(key)

        if self.storage[index] is None:
            self.storage[index] = LinkedPair(key, value)
        else:
            newItem = LinkedPair(key, value)
            newItem.next = self.storage[index]
            self.storage[index] = newItem

    def remove(self, key):
        index = self._hash_mod(key)

        if not self.storage[index]:
            print('Warning: Nothing to remove')
        elif self.storage[index].next:
            self.storage[index] = self.storage[index].next
        else:
            self.storage[index] = None

    def retrieve(self, key):
        index = self._hash_mod(key)

        if not self.storage[index]:
            return None
        else:
            output = self.storage[index]
            while output.next and output.key is not key:
                output = output.next
            if output.key is not key:
                return None
            else:
                return output.value

    def resize(self):
        tmpStore = self.storage
        self.capacity *= 2
        self.storage = [None]*(self.capacity)
        for i in range(self.capacity//2):
            if tmpStore[i]:
                while tmpStore[i].next:
                    self.insert(tmpStore[i].key, tmpStore[i].value)
                    tmpStore[i] = tmpStore[i].next
                self.insert(tmpStore[i].key, tmpStore[i].value)


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
