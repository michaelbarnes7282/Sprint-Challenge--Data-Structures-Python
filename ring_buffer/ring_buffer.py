import collections
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = collections.deque(maxlen=capacity)


    def append(self, item):
        self.storage.append(item)

    def get(self):
        return self.storage[0]