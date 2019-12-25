# implement lrucache with ordereddict,
# put and get methods all take O(1) time

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.conso = 0
        self.memo = OrderedDict()
        
    def get(self, key: int) -> int:
        if key not in self.memo:
            return -1
        
        val = self.memo[key]
        self.memo.pop(key)
        self.memo[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.memo:
            self.memo.pop(key)
            self.memo[key] = value
        else:
            if self.conso == self.cap:
                self.memo.popitem(last=False)
                self.conso -= 1

            self.memo[key] = value
            self.conso += 1
