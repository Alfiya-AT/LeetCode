class Solution(object):
    def reverseByType(self, s):
        special=[]
        alpha=[]
        for ch in s:
            if ch.isalpha():
                alpha.append(ch)
            else:
                special.append(ch)
        res=list(s)
        alpha.reverse()
        special.reverse()
        a=0
        sp=0
        for i in range(len(res)):
            if res[i].isalpha():
                res[i]=alpha[a]
                a+=1
            else:
                res[i]=special[sp]
                sp+=1
            
        return "".join(res)