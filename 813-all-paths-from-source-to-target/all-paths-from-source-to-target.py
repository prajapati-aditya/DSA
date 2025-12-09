class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        n = len(graph)
        result = []
        curr_path = []

        def dfs(node):
            curr_path.append(node)

            if node == n - 1:      
                result.append(curr_path.copy())
            else:
                for neighbour in graph[node]:
                    dfs(neighbour)

            curr_path.pop()           

        dfs(0)
        return result