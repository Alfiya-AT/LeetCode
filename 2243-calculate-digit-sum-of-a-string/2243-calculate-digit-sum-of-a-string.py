class Solution(object):
    def digitSum(self, s, k):

        def recursion(s, k):
            ans = []

            for i in range(0, len(s), k):
                group = s[i:i+k]

                total = 0
                for ch in group:
                    total += int(ch)

                ans.append(str(total))

            return "".join(ans)

        while len(s) > k:
            s = recursion(s, k)

        return s