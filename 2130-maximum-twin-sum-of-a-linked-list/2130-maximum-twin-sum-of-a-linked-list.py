# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        l=[]

        while head != None:
            l.append(head.val)
            head=head.next

        i=0
        j=len(l)-1

        mx=float('-Inf')

        while i<j:
            candidate=l[i]+l[j]
            mx=max(mx,candidate)

            i+=1
            j-=1

        return mx