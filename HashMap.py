#Source: used from video "Phyton: Creating a HashMap using lists" as recommended from the WGU course tips

class HashMap:
    def __init__(self):
        # Size of array
        self.size = 100
        #Array
        self.map = [None] * self.size

    # Takes key and calculates index then returns that index
    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    # Add function
    def add(self, key, value):
        # index value
        key_hash = self._get_hash(key)
        # list of the key and value
        key_value = [key, value]

        # Check if index is empty
        if self.map[key_hash] is None:

            # if empty add list into cell
            self.map[key_hash] = list([key_value])
            return True

        # if not empty, add into cell.
        else:

            # check if key and value is already in the list
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] == value
                    return True
            # if not yet in the list, add it.
            self.map[key_hash].append(key_value)

    # Get function
    def get(self, key):
        key_hash = self._get_hash(key)

        # check if hash key is not empty
        if self.map[key_hash] is not None:

            # if not empty iterate through, locate key and return value
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1];
        return None

    # Delete function
    def delete(self,key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range (0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    # Print function
    def print(self):
        print('test')
        for item in self.map:
            if item is not None:
                print(str(item))
