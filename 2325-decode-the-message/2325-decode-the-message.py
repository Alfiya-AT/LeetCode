class Solution(object):
    def decodeMessage(self, key, message):
        d={}
        val=97
        for i in key:
            if i.isalpha() and i not in d:
                d[i]=chr(val)
                val+=1
        res=""
        for ch in message:
            if ch.isalpha():
                res+=d[ch]
            else:
                res+=" "
        return res