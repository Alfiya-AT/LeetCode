class Solution(object):
    def shortestToChar(self, s, c):
        
        n=len(s)
        res=[float('inf')]*n
        last=float('-inf')

        for i in range(n):
            if s[i]==c:
                last=i
            res[i]=i-last

        last=float('inf')

        for i in range(n-1,-1,-1):
            if s[i]==c:
                last=i
            res[i]=min(res[i],last-i)

        return res



        # if c not in s:
        #     return 
        # res=[0]*len(s)
        # ptr1=s.index(c)
        # ptr2=s.index(c)
        # for i in range(len(s)):
        #     if i>ptr1 and i<ptr2:
        #         res[i]=min(abs(ptr1-i),abs(ptr2-i))
        #     elif i>ptr2:
        #         ptr1=ptr2
        #         while ptr2<len(s) and s[ptr2]!=c:
        #             ptr2+=1
        #     else:
        #         res[i]=abs(i-ptr1)
        # return res

        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        # idxC=[i for i in range(len(s)) if s[i]==c]
        
        # res=[]
        # ptrC=0
        # for ptrS in range(len(s)):
        #     if idxC[ptrC]>ptrS:
        #         res.append(abs(idxC[ptrC]-ptrS))
        #     elif idxC[ptrC]==ptrS:
        #         res.append(0)
        #         ptrC+=1
        # return res