# Uses python3

import sys


def number_of_components(adj):
    visited = {}
    cc = 0

    def explore(v):
        visited[v] = True
        for u in adj[v]:
            if visited.get(u, 0) == 0:
                explore(u)
        return 1

    for i in range(len(adj)):
        if visited.get(i, 0) == 0:
            cc += explore(i)

    return cc


if __name__ == '__main__':
    # input = sys.stdin.read()
    input = input()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))

# '4 4 1 2 3 2 4 3 1 4 1 4'
# 4 2 1 2 3 2 1 4
# 4 5 2 1 4 3 1 4 2 4 3 2 1 3
#6 3 1 2 3 4 5 6
