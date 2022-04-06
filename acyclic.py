# Uses python3

import sys


def acyclic(adj):
    visited = {}

    def explore(v):

        visited[v] = 1
        for u in adj[v]:
            if visited.get(u, 0) == 0:
                return explore(u)
            elif visited.get(u, 0) == 1:
                return 1
        return 0

    for i in range(len(adj)):
        if visited.get(i, 0) == 0:
            res = explore(i)
            if res == 1:
                return res

    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))

# 4 4 1 2 4 1 2 3 3 1
# 5 4 1 2 2 3 3 4 4 2
# 5 7 1 2 2 3 1 3 3 4 1 4 2 5 3 5
