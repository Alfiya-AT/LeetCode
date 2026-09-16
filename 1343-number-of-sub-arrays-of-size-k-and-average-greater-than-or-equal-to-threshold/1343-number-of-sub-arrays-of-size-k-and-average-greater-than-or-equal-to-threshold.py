class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):

        # mt=k*threshold
        # count=0
        # for i in range(len(arr)-k+1):
        #     currSum=0

        #     for j in range(i,i+k):
        #         currSum+=arr[j]

        #     if currSum>=mt:
        #         count+=1

        # return count


        mxt=k*threshold
        currSum=sum(arr[:k])
        count= 1 if currSum>=mxt else 0

        for i in range(k,len(arr)):
            currSum=currSum-arr[i-k]+arr[i]

            if currSum>=mxt:
                count+=1
            
        return count