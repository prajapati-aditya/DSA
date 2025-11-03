# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        curr = head
        while curr :
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            # now prev becomes new head and head becomes tail
        return prev



        