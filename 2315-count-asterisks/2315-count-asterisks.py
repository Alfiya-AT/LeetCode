class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        l=s.split("|")
        for i in range(0,len(l),2):
            for ch in l[i]:
                if ch=="*":
                    count+=1

        return count