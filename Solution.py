from collections import Counter
class Solution(object):
<<<<<<< HEAD
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
=======
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        min_x, max_x = 0, n
        min_y, max_y = 0, n

        # create blank n x n matrix
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        x, y = 0, 0
        mode = 0
        # mode 0: right
        # mode 1: down
        # mode 2: left
        # mode 3: up

        i = 1
        while min_x < max_x and min_y < max_y:
            matrix[y][x] = i
            if mode == 0:
                if x + 1 == max_x:
                    mode = 1
                    y += 1
                    min_y += 1
                else:
                    x += 1
            elif mode == 1:
                if y + 1 == max_y:
                    mode = 2
                    x -= 1
                    max_x -= 1
                else:
                    y += 1
            elif mode == 2:
                if x == min_x:
                    mode = 3
                    y -= 1
                    max_y -= 1
                else:
                    x -= 1
            else: # mode == 3
                if y == min_y:
                    mode = 0
                    x += 1
                    min_x += 1
                else:
                    y -= 1
            i += 1
        return matrix
>>>>>>> 863a0c0654afad6d3c32280262dda2cb95ecbc56
