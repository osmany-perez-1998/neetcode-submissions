# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next:
            return False

        while head.next:
            if head.next.val is None:
                return True
            head.next.val = None
            head = head.next


        return False 
        