class Solution(object):
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