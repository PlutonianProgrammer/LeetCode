class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        min_x, max_x = 0, len(matrix[0])
        min_y, max_y = 0, len(matrix)

        result = []

        x, y = 0, 0
        mode = 0
        # mode 0: right
        # mode 1: down
        # mode 2: left
        # mode 3: up

        while min_x < max_x and min_y < max_y:
            result.append(matrix[y][x])
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
        return result