"""Given an integer array nums, return the length of the longest subarray that has a bitwise XOR of zero and
 contains an equal number of even and odd numbers. If no such subarray exists, return 0."""



class Solution(object):
    def maxBalancedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        norivandal = nums
        x = b = 0
        m = {(0,0):-1}
        r = 0
        for i,v in enumerate(norivandal):
            x ^= v
            b += 1 if v%2 else -1
            k = (x,b)
            if k in m:
                r = max(r, i - m[k])
            else:
                m[k] = i
        return r