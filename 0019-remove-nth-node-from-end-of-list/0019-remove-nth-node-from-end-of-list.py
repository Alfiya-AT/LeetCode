# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # dummy = ListNode(0)
        # dummy.next=head

        # length=0
        # l=head
        # while l:
        #     length+=1
        #     l=l.next
        
        # d=length-n
        # prev=dummy
        # curr=head

        # i=0
        # while i<d:
        #     i+=1
        #     curr=curr.next
        #     prev=prev.next

        # prev.next=curr.next
        # return dummy.next

        # using 2 ptr

        dummy=ListNode(0)
        dummy.next=head

        l=head
        jump=0

        while jump<n and l!=None:
            l=l.next
            jump+=1

        prev=dummy
        curr=l

        while curr!=None:
            curr=curr.next
            prev=prev.next

        prev.next=prev.next.next

        return dummy.next