# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        return self.helper(ListNode(head.val, None), head.next)

        
    def helper(self, new: Optional[ListNode], old: Optional[ListNode]) -> Optional[ListNode]:
        if old is None:
            return new

        return self.helper(ListNode(old.val, new), old.next)
        