class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        # set1=set(s1.split(" "))
        # set2=set(s2.split(" "))

        # return list(set1^set2)

        l1=s1.split(" ")
        l2=s2.split(" ")
        d={}
        for i in range(max(len(l1),len(l2))):
            if i<len(l1):
                d[l1[i]]=d.get(l1[i],0)+1
            if i<len(l2):
                d[l2[i]]=d.get(l2[i],0)+1
        res=[]
        for key,value in d.items():
            if value==1:
                res.append(key)

        return res