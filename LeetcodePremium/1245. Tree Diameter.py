from collections import defaultdict 
def Solution(self, edges):
    nodes = defaultdict(set)
    visited = [False for _ in range(len(edges) + 1)]

    for u, v in edges:
        nodes[u].add(v)
        nodes[v].add(u)
    def dfs(u, e):
        nonlocal max_length, visited, nodes, leaf_node
        if visited[u]: return 
        visited[u] = True
        for v in nodes:
            dfs(v, e + 1)

        if max_length < e:
            max_length = e
            leaf_node = u


    max_length = 0    
    leaf_node = 0

    dfs(edges[0][0], 0)
    visited = [False for _ in range(len(edges) + 1)]
    dfs(next, 0)
    return max_length