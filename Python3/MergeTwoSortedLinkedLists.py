# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # A diagram of this solution
    # (Dummy) -> (1) -> (1) -> (2) -> (3) -> (4) -> (5)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # We start by making a dummy node we will branch off of
        # This is to avoid edge cases like empty lists, etc
        dummy_node = ListNode()
        # The tail of our linked list will start here at the dummy list, this is where we will
        # start pointing to our merged list
        tail = dummy_node
        # While both lists aren't empty
        while list1 and list2:
            # If list1's value is greater
            if list1.val < list2.val:
                # Then the next node in our list should be this node
                tail.next = list1
                # And then go to the next node in list1
                list1 = list1.next
            else:
                # Then the next node in our list should be this node
                tail.next = list2
                # And then go to the next node in list2
                list2 = list2.next
            # We will ALWAYS add a node, so once we do we need to update where the next node will go
            tail = tail.next

        # And then we are not guaranteed that our lists will be the same size
        # In the event that they are not, whatever is left over can just be appended to
        # the end of our list, since it is already sorted it will already be in the right order
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        # And then so we don't include the dummy node in our merged list
        # We have to return starting from the node right after the dummy
        return dummy_node.next
            