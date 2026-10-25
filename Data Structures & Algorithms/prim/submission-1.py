class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        for src, dest, wt in edges:
            adj[src].append((wt, dest))
            adj[dest].append((wt, src))
        
        res = 0
        minHeap = [(0, 0)]
        visited = set()

        while minHeap and len(visited) < n:
            wt, dest = heapq.heappop(minHeap)
            if dest in visited:
                continue
            res += wt
            visited.add(dest)

            for neighWt, neighbor in adj[dest]:
                heapq.heappush(minHeap, (neighWt, neighbor))

        return res if len(visited) == n else -1