# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def reverse(head: ListNode) -> ListNode:
            first = head
            pivot =head

            while pivot.next:
                aux = pivot.next
                pivot.next = aux.next

                aux.next = first
                first = aux

            return first

        def alternate(head1: ListNode, head2: ListNode):

            pivot1 = head1
            pivot2 = head2

            while pivot1 and pivot2:
                aux1 = pivot1.next
                aux2 = pivot2.next

                pivot1.next = pivot2
                pivot2.next = aux1

                pivot1 = aux1
                pivot2 = aux2


        if not head.next or not head.next.next:
            return

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next


        sec_half = reverse(slow.next)
        slow.next = None

        alternate(head,sec_half)
        