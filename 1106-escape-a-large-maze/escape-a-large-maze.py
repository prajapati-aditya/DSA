class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked = set(tuple(p) for p in blocked)
        limit = 20000
        def dfs(start,end) :
            q = deque([tuple(start)])
            visited = set([tuple(start)])
            dirs = [(1,0), (-1,0), (0,1), (0,-1)]

            while q :
                x,y = q.popleft()
                if [x,y] == end :   # reached end
                    return True
                if len(visited) > limit :   # traversed outside the box
                    return True
                
                for dx,dy in dirs :
                    nx,ny = dx+x, dy+y 
                    # check for the scope
                    if 0 <=nx< 10**6 and 0 <=ny< 10**6 :
                        if (nx,ny) not in visited and (nx,ny) not in blocked :
                            visited.add((nx,ny))
                            q.append((nx,ny))
            return False
        return dfs(source,target) and dfs(target,source)
                
            