class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans=[]

        def bt(i:int, cur:list[int], remaining:int):
            if remaining == 0:
                ans.append(cur[:])
                return 

            if remaining<0 or i>=len(candidates):
                return 


            cur.append(candidates[i])
            bt(i,cur,remaining-candidates[i])
            cur.pop()

            bt(i+1,cur,remaining)
            
        bt(0,[],target)

        return ans





























        # def subset(arr,i,t,ans,combin,setS):
            
        #     if(idx==arr.size() or t<0):
        #         return 
            

        #     if(t==0):
        #         if combin not in setS:
        #             ans.push(combin)
        #         return 
            
        #     combin.push(arr[i])
        #     subset(arr,i+1,tar-arr[i],ans,combin,setS)

        #     subset(arr,i,tar-arr[i],ans,combin,setS)
        #     combin.pop()

        #     subset(arr,i+1,tar,ans,combin,setS)

        # setS=set()    
        # ans=[]
        # combin=[]
        # subset(candidates,0,ans,combin,setS)

        # return setS

