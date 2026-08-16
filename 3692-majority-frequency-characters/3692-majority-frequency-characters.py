class Solution(object):
    def majorityFrequencyGroup(self, s):
        """
        :type s: str
        :rtype: str
        """
        # s = "aaabbbccccdddde"
        n=len(s)
        freq=[""]*n
        d={}
        for i in s:
            d[i]=d.get(i,0)+1

        for key,val in d.items():
            idx=val-1
            freq[idx]+=key

        arr1=freq
        arr1=sorted(arr1,key=len)
        mx=len(arr1[-1])

        for i in range(n-1,-1,-1):
            if len(freq[i])==mx:
                return (freq[i])
                
        