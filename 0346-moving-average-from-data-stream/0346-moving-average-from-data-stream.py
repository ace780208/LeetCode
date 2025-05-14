from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.queue = deque()
        self.window_size = size
        self.total = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.total += val
        while len(self.queue) > self.window_size:
            self.total -= self.queue.popleft()
        return self.total/len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)