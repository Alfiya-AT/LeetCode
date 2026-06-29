from itertools import chain
class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        

        arr=[0,0]

        l=list(chain(*grid))

        sumL=sum(l)
        n=len(l)

        actualSum=(n*(n+1))//2
        for i in range(len(l)):
            if l[i] in l[i+1:]:
                repeat=l[i]
                break
        arr[1]=abs((sumL-repeat)-actualSum)
        arr[0]=repeat

        return arr