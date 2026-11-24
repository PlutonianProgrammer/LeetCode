class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1 or len(s) <= numRows:
            return s
        res_arr = []
        m = numRows - 1
        for start_idx in range(numRows):
            res_arr.append(s[start_idx])
            mag = 2 * (m - start_idx)
            i = start_idx
            even = True
            while True:
                increment = mag if even else 2 * m - mag
                even = not even
                if not increment:
                    continue
                i += increment
                if not i < len(s):
                    break
                res_arr.append(s[i])

        return ''.join(res_arr)

s = 'PayPalIsHiring'
numRows = 2
print(Solution().convert(s, numRows))