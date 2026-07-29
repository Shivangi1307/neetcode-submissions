"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None

        curr = head
        node_copy = {}

        while curr:

            copy = Node(curr.val)
            node_copy[curr] = copy
            curr = curr.next

        curr = head

        while curr:

            copy = node_copy[curr]
            copy.next = node_copy.get(curr.next)
            copy.random = node_copy.get(curr.random)

            curr = curr.next

        return node_copy[head]

