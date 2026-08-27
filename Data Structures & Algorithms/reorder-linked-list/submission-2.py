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
            aux.next = prev
            prev = aux

        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head or not head.next: return
        
        fst = head
        mid = None
        odd_count = True
        last = None
       

        slow_pointer = head
        fast_pointer = head

        while fast_pointer.next:

            if fast_pointer.next.next:
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next.next
            else:
                odd_count= False
                last = slow_pointer.next

                slow_pointer.next = slow_pointer.next.next                
                break

        mid = slow_pointer

        mid.next = self.reverseList(mid.next)

        while mid.next:
            aux1 = fst.next
            aux2 = mid.next
            mid.next = aux2.next

            fst.next = aux2
            fst.next.next = aux1
            fst = aux1

        if not odd_count:
            mid.next = last
            last.next = None
        

        

        