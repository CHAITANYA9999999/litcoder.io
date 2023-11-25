class Solution:
    def clumsy(self, n: int) -> int:
        dic = {3:6, 2:2, 1:1, 0:0}
        if n<4:
            return dic[n]
        total = (n*(n-1))//(n-2) + n-3
        n-=4
        while n>=4:
            total = total - (n*(n-1))//(n-2) + n-3
            n -= 4
        return total - dic[n]