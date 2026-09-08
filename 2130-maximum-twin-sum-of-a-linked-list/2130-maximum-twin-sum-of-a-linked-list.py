class Solution(object):

    def reverseLL(self, node):
        curr = node
        prev = None

        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """

        # Step 1: Find the middle of the linked list
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        p2 = self.reverseLL(slow)
        p1 = head

        # Step 3: Find maximum twin sum
        mx = float('-inf')

        while p1 != None and p2 != None:
            candidate = p1.val + p2.val
            mx = max(mx, candidate)

            p1 = p1.next
            p2 = p2.next

        return mx