# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head :
            return head
        length = 1 
        tail = head
        while tail.next :
            length += 1
            tail = tail.next
        # curr in=s now at the last node
        
        k = k % length
        if k == 0 :
            return head
        curr = head
        for i in range(length-k-1) :
            curr = curr.next
        newHead = curr.next # means now 4 beomes the new head
        curr.next = None    # now me make 3 the last node 
        tail.next = head    # we put 5's next to be the pointing to 1
        return newHead
        