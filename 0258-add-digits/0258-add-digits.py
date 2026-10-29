class Solution:
    def addDigits(self, num: int) -> int:
        # if num<=9:
        #     return num
        
        # while num>9:
        #     res=num
        #     val=0
        #     while res>0:
        #         val+=res%10
        #         res//=10

        #     num=val
        
        # return num


        a=0

        for i in str(num):
            a+=int(i)

        if a>9:
            return self.addDigits(a)
        
        return a