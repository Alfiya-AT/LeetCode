class Solution(object):
    def sortSentence(self, s):
        # s = "is2 sentence4 This1 a3"
        sl=s.split()
        # print(sl)
        l=[0]*len(sl)
        for i in range(len(sl)):
            index=sl[i]
            l[int(index[-1])-1]=index[:-1]
        res=" ".join(l)
        return res

