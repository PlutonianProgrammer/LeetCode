class Solution(object):
<<<<<<< HEAD
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        adjecency_matrix = [[False for _ in range(n)] for _ in range(n)]

        # Put into adjecency matrix
        for edge in trust:
            adjecency_matrix[edge[0]-1][edge[1]-1] = True
        
        candidates = []

        # Add people who don't trust anyone
        for i in range(n):
            if True not in adjecency_matrix[i]:
                candidates.append(i)
        
        # Remove any candidates not trusted by all
        for candidate in candidates[:]:
            for i in range(n):
                if i != candidate and adjecency_matrix[i][candidate] == False:
                    candidates.remove(candidate)
                    break

        if candidates:
            return candidates[0] + 1
        else:
            return -1

n = 4
trust = [[1,3],[1,4],[2,3]]
print(Solution().findJudge(n, trust))
=======
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
>>>>>>> 8b9b6e3e3a3c5227fea4817885742943ed3bbb5f
