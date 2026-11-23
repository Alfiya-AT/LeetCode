# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    
    def removeNodes(self, head: ListNode | None) -> ListNode | None:
        
    
        def reverse(node: ListNode | None) -> ListNode | None:
            prev=None
            curr=node

            while curr:
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt

            return prev
        

        rev_head=reverse(head)


        max_val=float("-inf")
        dummy = ListNode(0)

        tail=dummy
        curr=rev_head

        while curr:
            nxt=curr.next
            curr.next=None
            if curr.val>=max_val:
                max_val=curr.val
                tail.next=curr
                tail=curr
            curr=nxt

        return reverse(dummy.next)        