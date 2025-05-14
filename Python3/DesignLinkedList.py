class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.left = Node(0)
        self.right = Node(0)
        # Dummy nodes to help with edge cases
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        # Start with our first real data point
        cur = self.left.next
        # While we have a valid node AND more to decrement
        while cur and index > 0:
            # Move to the next node in the list and decrement
            cur = cur.next
            index -= 1
        # If our current node is valid, and it's real data (not dummy) and we went the entire requested length
        if cur and cur != self.right and index == 0:
            # Then success and return our current value
            return cur.val
        else:
            # Otherwise something went wrong and we are invalid
            return -1

    def addAtHead(self, val: int) -> None:
        # Since we have dummy nodes, this is easy
        # We just add the node after left and move the pointers
        node, next, prev = Node(val), self.left.next, self.left
        # Point into node
        prev.next = node
        next.prev = node
        # Point out of node
        node.next = next
        node.prev = prev

    def addAtTail(self, val: int) -> None:
        # Since we have dummy nodes, this is easy
        # We just add the node before right and move the pointers
        node, next, prev = Node(val), self.right, self.right.prev
        # Point into node
        prev.next = node
        next.prev = node
        # Point out of node
        node.next = next
        node.prev = prev

    def addAtIndex(self, index: int, val: int) -> None:
        # Start at our first valid not dummy node
        cur = self.left.next
        # While our node is non null and our index has more to go
        # Increment through the list
        while cur and index > 0:
            cur = cur.next
            index -= 1
        # If the value we land on is valid, and we exhausted the index
        if cur and index == 0:
            node, next, prev = Node(val), cur, cur.prev
            # Point into node
            prev.next = node
            next.prev = node
            # Point out of node
            node.next = next
            node.prev = prev


    def deleteAtIndex(self, index: int) -> None:
        # Start at our first valid not dummy node
        cur = self.left.next
        # While our node is non null and our index has more to go
        # Increment through the list
        while cur and index > 0:
            cur = cur.next
            index -= 1
        # If the value we land on is valid, and we exhausted the index
        # A key difference here is our dummy nodes are INVALID for this case
        if cur and cur != self.right and index == 0:
            next, prev = cur.next, cur.prev
            next.prev = prev
            prev.next = next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)