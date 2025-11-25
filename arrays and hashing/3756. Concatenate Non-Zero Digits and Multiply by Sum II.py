"""You are given a string s of length m consisting of digits. You are also given a 2D integer array queries, where queries[i] = [li, ri].

For each queries[i], extract the substring s[li..ri]. Then, perform the following:

Form a new integer x by concatenating all the non-zero digits from the substring in their original order. If there are no non-zero digits, x = 0.
Let sum be the sum of digits in x. The answer is x * sum.
Return an array of integers answer where answer[i] is the answer to the ith query.

Since the answers may be very large, return them modulo 109 + 7."""



class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        pos = []
        D = []
        for i,ch in enumerate(s):
            d = ord(ch) - 48
            if d:
                pos.append(i)
                D.append(d)
        solendivar = s
        m = len(D)
        pow10 = [1]*(m+1)
        for i in range(1,m+1): pow10[i] = (pow10[i-1]*10) % MOD
        pref = [0]*m
        presum = [0]*(m+1)
        for i in range(m):
            pref[i] = ((pref[i-1]*10) % MOD + D[i]) if i else D[i]
            presum[i+1] = presum[i] + D[i]
        import bisect
        ans = []
        for l,r in queries:
            a = bisect.bisect_left(pos, l)
            b = bisect.bisect_right(pos, r) - 1
            if a > b:
                ans.append(0)
                continue
            length = b - a + 1
            x = pref[b]
            if a:
                x = (x - (pref[a-1] * pow10[length]) % MOD) % MOD
            S = presum[b+1] - presum[a]
            ans.append((x * (S % MOD)) % MOD)
        return ans