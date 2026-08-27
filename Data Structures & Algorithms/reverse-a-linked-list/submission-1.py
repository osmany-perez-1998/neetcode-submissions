# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if not head : return None

        prev = head
        curr = head

        while curr.next:
            aux = curr.next
            curr.next = curr.next.next

            # if prev is None:
            #     aux.next = curr
            #     prev = aux
            # else:
            aux.next = prev
            prev = aux

        return prev
        