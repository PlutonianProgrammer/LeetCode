class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        
        num_provinces = 0
        explored = set()

        def dfs(node):
            explored.add(node)
            for other_node in range(len(isConnected[node])):
                if isConnected[node][other_node] != 0 and other_node not in explored:
                    dfs(other_node)

        for node in range(len(isConnected)):
            if node not in explored:
                dfs(node)
                num_provinces += 1
        
        return num_provinces
    
matrix = [[1,0,0],[0,1,0],[0,0,1]]
print(Solution().findCircleNum(matrix))