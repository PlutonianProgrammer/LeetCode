class Solution(object):
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