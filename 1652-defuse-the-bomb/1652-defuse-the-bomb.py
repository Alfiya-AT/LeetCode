class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:

        res=[0 for _ in range(len(code))]

        if k==0:
            return res

        start, end, window_sum=1,k,0


        if k<0:
            start=len(code)-abs(k)
            end=len(code)-1

        for i in range(start,end+1):
            window_sum+=code[i]

        for i in range(len(code)):
            res[i]=window_sum
            window_sum-=code[start%len(code)]
            window_sum+=code[(end+1)%len(code)]

            start+=1
            end+=1

        return res