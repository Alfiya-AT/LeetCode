class Solution(object):
    def findRepeatedDnaSequences(self, s):
        left=0
        right=9
        d=set()
        res=set()
        while right<len(s):
            if s[left:right+1] in d:
                res.add(s[left:right+1])
            else:
                d.add(s[left:right+1])
            left+=1
            right+=1

        return list(res)