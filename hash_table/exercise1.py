import random


class HashTable:
    def __init__(self, length=4):
        self.array = [None] * length

    def _hash(self, key):
        """Get the index of our array for a specific string key"""
        length = len(self.array)
        return hash(key) % length

    def set(self, key, value):
        address = self._hash(key)
        if self.array[address]:
            key_exist = False
            for x in self.array[address]:
                if x[0] == key:
                    x[1] = value
                    key_exist = True
                    break
            if not key_exist:
                self.array[address].append([key, value])
        else:
            self.array[address] = [[key, value]]

    def get(self, key):
        address = self._hash(key)
        if not self.array[address]:
            return None

        for kvp in self.array[address]:
            if kvp[0] == key:
                return kvp[1]


if __name__ == '__main__':
    obj = HashTable()
    obj.set("a", 1)
    obj.set("b", 6)
    obj.set("c", 10)
    obj.set("d", 6)
    obj.set("a", 10)
    value = obj.get("e")
    value = obj.get("a")
    print(value)
