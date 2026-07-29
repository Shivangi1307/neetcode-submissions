# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head

        start = dummy

        while True:

            curr = start

            for _ in range(k):
                curr = curr.next
                if not curr:
                    return dummy.next

            nextgroup = curr.next

            prev = nextgroup
            curr1 = start.next

            for _ in range(k):
                nxt = curr1.next
                curr1.next = prev
                prev = curr1
                curr1 = nxt
            
            temp = start.next
            start.next = prev
            start = temp

        return dummy.next

            
            

            

