class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        count=0
        for c in words:
            i=0
            flag=1
            if len(c)>=len(pref):
                for i in range(len(pref)):
                    if c[i]!=pref[i]:
                        flag=0
                        break
            
                if flag==1:
                    count+=1
            
        return count