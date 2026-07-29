# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        for _ in range(left - 1):
            prev = curr
            curr = curr.next

        tail = curr
        prev2 = None

        for _ in range(right - left + 1):

            nxt = curr.next
            curr.next = prev2
            
            prev2 = curr
            curr = nxt

        prev.next = prev2
        tail.next = curr

        return dummy.next
