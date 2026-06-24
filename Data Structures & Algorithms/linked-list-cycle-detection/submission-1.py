# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        return self.helper(head, 0)
    

    def helper(self, head: Optional[ListNode], length) -> bool:
        if not head.next:
            return False
        if head.next.val < length:
            return True
        return self.helper(head.next, length + 1)
        