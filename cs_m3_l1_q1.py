class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        s = set(pattern)
        if len(s)==1:
            n = text.count(pattern[0])
            return (n*(n+1))//2
        new_text=''
        for i in text:
            if i in s:
                new_text+=i
        p0=pattern[0]
        p1=pattern[1]
        p0_count = new_text.count(p0)
        p1_count = new_text.count(p1)
        dummy = p1_count
        total=0
        for alp in new_text:
            if alp == p0: 
                total += p1_count
            else:
                p1_count-=1
        return max(total + dummy, total + p0_count)