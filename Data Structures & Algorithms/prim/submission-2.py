class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for src, dest, wt in edges:
            adj[src].append((dest, wt))
            adj[dest].append((src, wt))

        minHeap = [(0, edges[0][0])]
        visited = set()
        res = 0

        while minHeap and len(visited) < n:
            wt, node = heapq.heappop(minHeap)

            if node in visited:
                continue

            visited.add(node)
            res += wt

            # Visit all neighbors of curr node
            for nei, dist in adj[node]:
                heapq.heappush(minHeap, (dist, nei))

        return res if len(visited) == n else -1