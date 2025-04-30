# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # We will keep track of the node before us
        prev = None
        # To start, if we don't even have a node there's no work for us
        if head:
            # While we have another node
            while head.next:
                # Store that next node in preparation
                next_node = head.next
                # If there was a previous node before us
                if prev:
                    # We want to point at it
                    head.next = prev
                else:
                    # Otherwise we are the new tail and should point nowhere
                    head.next = None
                # Now we are the current previous for the next node
                prev = head
                # And continue through the list
                head = next_node
            # We get here on the last node and all we need to do is
            # set our next to the previous and we're done
            if prev:
                head.next = prev

        return head