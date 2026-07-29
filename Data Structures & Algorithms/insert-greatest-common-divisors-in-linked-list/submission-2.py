# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from math import gcd
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        nxt = curr.next

        while nxt:
            
            val = gcd(curr.val,nxt.val)
            
            node = ListNode(val)

            curr.next = node
            node.next = nxt

            curr = node.next
            nxt = nxt.next

        return head
