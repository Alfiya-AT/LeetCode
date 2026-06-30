class Solution(object):
    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """
        eve=0
        odd=0
        for i in range(len(num)):
            if i%2==0:
                eve+=int(num[i])
            else:
                odd+=int(num[i])
        return odd==eve