from collections import deque

# This solution is focused on creating a correct and fast solution
class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        return self.q.pop()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0

# Alternate Solution

# This solution focuses on understanding what the problem is trying to teach us
class MyStack2:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        # Iterate through all but the last element, this will place the last element at the front of the queue
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())
        # And then return the leftmost element, which is out last element
        return self.q.popleft()


    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0
