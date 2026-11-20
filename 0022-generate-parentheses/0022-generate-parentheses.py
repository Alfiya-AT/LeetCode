class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        
        output=[]

        def build(curr,opened,close,n,output):
            if len(curr)==2*n:
                output.append("".join(curr))
                return 

            if opened<n:
                curr.append("(")
                build(curr,opened+1,close,n,output)
                curr.pop()

            if close < opened:
                curr.append(")")
                build(curr,opened,close+1,n,output)
                curr.pop()

        build([],0,0,n,output)
        return output