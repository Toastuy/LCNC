class MinStack:

    # Diagram example
    # stack    minimum
    # [-3]      [-3]
    # [0]       [-2]
    # [-2]      [-2]

    def __init__(self):
        # We need two data structures here to keep getMin() in O(1) time
        # One will track the values, one will track the minimum
        self.stack = []
        self.minimum = []

    def push(self, val: int) -> None:
        # Just append to our value stack
        self.stack.append(val)

        # But then we need to do some logic to figure out our min for our minimum
        # set value equal to the minimum of val and top of min stack if it is non empty
        # otherwise just keep value the same as it is now
        # this is how we deal with the first element!
        val = min(val, self.minimum[-1] if self.minimum else val)
        self.minimum.append(val)

    def pop(self) -> None:
        # Just pop from our value stack and our minimum
        # We are guaranteed non empty stacks when this is called
        self.stack.pop()
        self.minimum.pop()

    def top(self) -> int:
        # Just return the top value of our value stack
        # We are guaranteed non empty stacks when this is called
        return self.stack[-1]

    def getMin(self) -> int:
        # Just return the top of our minimum stack
        # We are guaranteed non empty stacks when this is called
        return self.minimum[-1]
