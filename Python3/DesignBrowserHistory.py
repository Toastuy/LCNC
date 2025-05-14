# This solution is the most verbose
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:
    def __init__(self, homepage: str):
        # All we will need is the page we are on, named cur
        self.cur = Node(homepage)

    def visit(self, url: str) -> None:
        # When we visit a homepage, we place it as the next to our current
        # And then change out cur to be that homepage
        self.cur.next = Node(url, self.cur)
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        # To move back, first we need to make sure we have a back
        # and then we decrement back to it and return
        while self.cur.prev and steps > 0:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val

    def forward(self, steps: int) -> str:
        # To move forward, first we need to make sure we have a forward
        # and then we increment to it and return
        # This part confused me because I wasn't sure how to "clear forward history"
        # BUT when we visit we are moving the pointers, and the next pointer becomes null
        # So the old forward history is automatically deleted when we visit with no extra work
        while self.cur.next and steps > 0:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val

# Alternate solution
# This solution is technically more efficient but circumvents the point of the problem
class BrowserHistory:
    def __init__(self, homepage: str):
        # This is our current pointer
        self.i = 0
        # The "true" length of our array
        # This is because we won't actually alter the length of our array
        # As we work on it, and instead overwrite old entries
        self.len = 1
        # And this is our history stack
        self.history = [homepage]

    def visit(self, url: str) -> None:
        # We need to add this url to the next position
        # First see if our history is long enough to just overwrite
        # If it isn't, then we append to the history instead
        if len(self.history) < self.i + 2:
            self.history.append(url)
        else:
            # So we can only do this if the position has already been filled before
            self.history[self.i + 1] = url
        # Then we just increment our current pointer and update our length
        self.i += 1
        self.len = self.i + 1

    def back(self, steps: int) -> str:
        # This is in a max call to make sure we don't go out of bounds
        # If it goes OUT of bounds, we instead just go to 0
        self.i = max(self.i - steps, 0)
        return self.history[self.i]

    def forward(self, steps: int) -> str:
        # This is in a max call to make sure we don't go out of bounds
        # If it goes OUT of bounds, we instead just go to the len - 1
        self.i = max(self.i + steps, self.len - 1)
        return self.history[self.i]