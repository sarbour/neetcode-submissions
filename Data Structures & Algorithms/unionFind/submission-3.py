class UnionFind:
    def __init__(self, n: int):
        self.par = {}
        self.rank = {}
        self.numComponents = n

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, x: int) -> int:
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        rootx, rooty = self.find(x), self.find(y)

        if rootx == rooty:
            return False

        if self.rank[rootx] > self.rank[rooty]:
            self.par[rooty] = rootx
        elif self.rank[rootx] < self.rank[rooty]:
            self.par[rootx] = rooty
        else:
            self.par[rooty] = rootx
            self.rank[rootx] += self.rank[rooty]
        self.numComponents -= 1
        return True

    def getNumComponents(self) -> int:
        return self.numComponents

