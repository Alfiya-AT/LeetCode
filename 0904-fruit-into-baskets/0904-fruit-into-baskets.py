class Solution(object):
    def totalFruit(self, fruits):
        
        # seen=set()
        # mx=0
        # i=0
        # k=0
        # for j in range(len(fruits)):
        #     seen.add(fruits[j])

        #     if len(seen)>2:
        #         seen.remove(fruits[k])
        #         k=i
        #     if fruits[i]!=fruits[j]:
        #         i=j

        #     mx=max(mx,j-k+1)
        
        # return mx


        mx=0
        d={}
        i=0
        for j in range(len(fruits)):
            d[fruits[j]]=d.get(fruits[j],0)+1

            while len(d)>2:
                d[fruits[i]]-=1
                if d[fruits[i]]==0:
                    d.pop(fruits[i])
                i+=1
            
            mx=max(mx,j-i+1)
        return mx