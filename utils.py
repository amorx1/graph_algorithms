
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] == x:
            return x

        return self.find(self.parent[x])

    def union(self, x, y):
        r1 = self.find(x)
        r2 = self.find(y)
        self.parent[r1] = r2