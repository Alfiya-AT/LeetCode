# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        

        if not head or not head.next:
            return 

        fast=head
        slow=head
        prev=None
        while fast is not None and fast.next is not None:
            fast=fast.next.next
            prev=slow
            slow=slow.next
        prev.next=slow.next

        return head