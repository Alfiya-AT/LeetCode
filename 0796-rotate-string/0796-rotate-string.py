class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s)!=len(goal):
            return False
        n=len(s)
        i=0
        # res=""
        while i<=n:
            res=s[i+1:]+s[:i+1]
            if res==goal:
                return True
            i+=1
        return False