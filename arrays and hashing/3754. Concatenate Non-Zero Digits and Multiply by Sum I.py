"""You are given an integer n.

Form a new integer x by concatenating all the non-zero digits of n in their original order. If there are no non-zero digits, x = 0.

Let sum be the sum of digits in x.

Return an integer representing the value of x * sum."""


class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        if(int(str(n).replace("0",""))):
            n=int(str(n).replace("0",""))
        else:
            n=0
        l=[int(d) for d in str(n)]
        s=sum(l)
        return s*n