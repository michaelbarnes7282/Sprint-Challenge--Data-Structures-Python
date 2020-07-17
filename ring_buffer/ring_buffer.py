from collections import deque
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []


    def append(self, item):
        newest = [item]
        if len(self.storage) < self.capacity:
            self.storage.append(item)
            newest[0] = item
        else:
            i = self.storage.index(newest[0])
            self.storage[i] = item
            newest.remove(newest[0])
            newest.append(item)

    def get(self):
        return self.storage