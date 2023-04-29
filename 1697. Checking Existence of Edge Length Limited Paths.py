# # An undirected graph of n nodes is defined by edgeList, where edgeList[i] = [ui, vi, disi] denotes an edge between nodes ui and vi with distance disi. Note that there may be multiple edges between two nodes.

# # Given an array queries, where queries[j] = [pj, qj, limitj], your task is to determine for each queries[j] whether there is a path between pj and qj such that each edge on the path has a distance strictly less than limitj .

# # Return a boolean array answer, where answer.length == queries.length and the jth value of answer is true if there is a path for queries[j] is true, and false otherwise.

# Input: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
# Output: [false,true]
# Explanation: The above figure shows the given graph. Note that there are two overlapping edges between 0 and 1 with distances 2 and 16.
# For the first query, between 0 and 1 there is no path where each distance is less than 2, thus we return false for this query.
# For the second query, there is a path (0 -> 1 -> 2) of two edges with distances less than 5, thus we return true for this query.
# Constraints:

# 2 <= n <= 105
# 1 <= edgeList.length, queries.length <= 105
# edgeList[i].length == 3
# queries[j].length == 3
# 0 <= ui, vi, pj, qj <= n - 1
# ui != vi
# pj != qj
# 1 <= disi, limitj <= 109
# There may be multiple edges between two nodes.

# solution :::
  class Solution :
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        parent = [i for i in range(n+1)]
    
        rank = [0 for i in range(n+1)]

        def find(parent, x):

            if parent[x] == x:
                return x
            parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent, a, b):

            a = find(parent, a)
            b = find(parent, b)

            if a == b:
                return 

            if rank[a] < rank[b]:
                parent[a] = b
            elif rank[a] > rank[b]:
                parent[b] = a
            else:
                parent[b] = a
                rank[a] += 1
                
        edgeList.sort(key = lambda x: x[2])
        res = [0] * len(queries)
        queries = [[i, ch] for i, ch in enumerate(queries)]
        queries.sort(key = lambda x: x[1][2])
        
        ind = 0
        for i, (a, b, w) in queries:
            
            while ind < len(edgeList) and edgeList[ind][2] < w:
                union(parent, edgeList[ind][0], edgeList[ind][1])
                ind += 1
                
            res[i] = find(parent, a) == find(parent, b)
        return res
