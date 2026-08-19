class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        freq1={}
        freq2={}
        for i in word1:
            freq1[i]=freq1.get(i,0)+1

        for j in word2:
            freq2[j]=freq2.get(j,0)+1
        
        # n=len(word1)
        # for i in range(n):
        #     if (word1[i] in word2) and( abs(freq1[word1[i]]-freq2[word1[i]])>3):
        #         return False
        #     if (word2[i] in word1 )and (abs(freq1[word2[i]]-freq2[word2[i]])>3):
        #         return False
        #     elif( freq1[word1[i]]>3 ) or (freq2[word2[i]]>3):
        #         return False
        

        for ch in set(word1+word2):
            f1=freq1.get(ch,0)
            f2=freq2.get(ch,0)

            if abs(f1-f2)>3:
                return False
        return True