class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        visited = set()
        visiting = set()

        for src, dest in edges:
            adj[src].append(dest)
        
        res = []

        def dfs(node):
            if node in visited:
                return True
            if node in visiting:
                return False

            visiting.add(node)

            for nei in adj[node]:
                if not dfs(nei):
                    return False

            visiting.remove(node)
            visited.add(node)
            res.append(node)

            return True

        for i in range(n):
            if not dfs(i):
                return []

        return res[::-1]