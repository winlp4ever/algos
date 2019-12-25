import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.hash = dict()
        self.size = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.hash:
            return False
        self.stack.append(val)
        self.hash[val] = self.size
        self.size += 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.hash:
            return False
        i = self.hash[val]
        if i < self.size-1:
            v = self.stack[-1]
            self.stack[i], self.stack[-1] = self.stack[-1], self.stack[i]
            self.hash[v] = i

        self.stack.pop()
        self.hash.pop(val)
        
        self.size -= 1
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        i = random.randint(0, self.size-1)
        return self.stack[i]
        