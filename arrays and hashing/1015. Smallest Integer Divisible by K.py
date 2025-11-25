"""Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.

Return the length of n. If there is no such n, return -1.

Note: n may not fit in a 64-bit signed integer."""



class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k==2 or k==5:
            return -1
        t=0
        for i in range(1,k+1):
            t=(t*10+1)%k
            if t==0:
                return i
        return -1
