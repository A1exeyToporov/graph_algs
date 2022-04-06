# Uses python3

import sys


def reach(adj, x, y):
    visited = {y: 0}

    def explore(v):
        visited[v] = 1
        for u in adj[v]:
            if visited.get(u, 0) == 0:
                explore(u)

    explore(x)
    return visited[y]


if __name__ == '__main__':
    # input = sys.stdin.read()
    input = input()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    visited = {}
    print(reach(adj, x, y))

# '4 4 1 2 3 2 4 3 1 4 1 4'
# 4 2 1 2 3 2 1 4
# 4 5 2 1 4 3 1 4 2 4 3 2 1 3
