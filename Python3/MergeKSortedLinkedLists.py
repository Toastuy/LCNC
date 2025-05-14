# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # First handle edge cases
        if not lists or len(lists) == 0:
            return None

        # Take pairs of linked list and merge them each time until 1 linked list left
        # We are doing GREATER THAN one, because if it's just one we're done
        while len(lists) > 1:
            output = []

            # Incrementer is 2 because we want pairs
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # Make sure we're not going out of bounds
                l2 = lists[i + 1] if (i+1) < len(lists) else None
                output.append(self.mergeList(l1, l2))
            lists = output
        return lists[0]
        
    def mergeList(self, l1, l2):
        # This is from another problem and we have solved it before
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        
        return dummy.next
        
            