class UnionFind:
    
    def __init__(self, n: int):
        self.par = {}
        self.rank = {}
        self.numComponents = n

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, x: int) -> int:
        curP = self.par[x]
        while curP != self.par[curP]:
            self.par[curP] = self.find(curP)
            curP = self.par[curP]
        return curP

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        rootX, rootY = self.find(x), self.find(y)

        if rootX == rootY:
            return False

        if self.rank[rootX] < self.rank[rootY]:
            self.par[rootX] = rootY
            self.rank[rootY] += self.rank[rootX]
        if self.rank[rootX] > self.rank[rootY]:
            self.par[rootY] = rootX
            self.rank[rootX] += self.rank[rootY]
        else:
            self.par[rootX] = rootY
            self.rank[rootY] += 1
        self.numComponents -= 1
        return True

    def getNumComponents(self) -> int:
        return self.numComponents