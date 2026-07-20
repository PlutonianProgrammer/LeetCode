from collections import Counter
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        def recursive_split(str):
            print(str)
            if len(str) < k:
                return 0
            counts = Counter(str)
            imperfect = False
            for val in counts.values():
                if val < k:
                    imperfect = True
            if not imperfect:
                return len(str)
            prev_i = -1
            max_sub_length = 0
            for i in range(len(str)):
                if counts[str[i]] < k:
                    max_sub_length = max(max_sub_length, recursive_split(str[prev_i+1:i]))
                    prev_i = i
            return max(max_sub_length, recursive_split(str[prev_i+1:i+i]))

        return recursive_split(s)
        
print(Solution().longestSubstring("bbaaacbd", 3))