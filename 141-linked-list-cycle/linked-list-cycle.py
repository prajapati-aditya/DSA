# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: # edge cases if there is no head or just one  node
            return False
        slow,fast = head, head.next   # initialize both pointers
        while fast and fast.next:   # while both fast and it's next node exist
                                    # if it doesn't exist means it ends without loop
            if slow == fast:
                return True
            slow=slow.next
            fast= fast.next.next    # fast pointer runs two steps ahead
        return False
        