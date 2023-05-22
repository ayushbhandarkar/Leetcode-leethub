class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        N =len(s)

        c= list(s)
        for i in range(N):
            if c[i] !=c[N-i-1]:
                d=min(c[i],c[N-i-1])
                c[i]=c[N-i-1]=d

        return"".join(c)


