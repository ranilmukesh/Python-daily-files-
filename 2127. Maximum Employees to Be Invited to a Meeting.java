class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        indegree = [0 for i in range(n)]
        for u in favorite:
            if u == -1:
                continue
            indegree[u] += 1

        depth = [1] * n
        for u in range(n):
            temp = 1
            while indegree[u] == 0 and favorite[u] != -1:
                v = favorite[u]
                favorite[u] = -1
                indegree[v] -= 1
                depth[v] =max(depth[v], 1 + depth[u])
                u = v
    
        visited, res, total_link_loop_2 = set(), 0, 0
        for u in range(n):
            if indegree[u] == 0 or u in visited:
                continue
            ans = 0
            while favorite[u] not in visited:
                visited.add(favorite[u])
                v = favorite[u]
                ans += 1
                u = v
            if ans == 2:
                total_link_loop_2 += depth[u] +depth[favorite[u]]
            elif ans >= 3:
                res = max(res, ans)
        return max(res, total_link_loop_2)
