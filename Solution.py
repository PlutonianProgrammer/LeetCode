class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Transpose Matrix
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if y < x:
                    # Swap each element above main diagonal with respective element below
                    matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]

        # Reverse Rows
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]


print('test')