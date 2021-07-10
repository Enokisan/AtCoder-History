from collections import deque

N, Q = list(map(int, input().split()))
graph = [[] for _ in range(N)]

def bfs(s, g):
    dist = [-1] * N
    d = deque()
    d.append(s)
    dist[s] = 0

    while d:
        v = d.popleft()
        for i in range(len(graph[v])):
            if dist[graph[v][i]] == -1:
                dist[graph[v][i]] = dist[v] + 1
                d.append(i)
    
    return dist[g]

for i in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

for i in range(Q):
    c, d = list(map(int, input().split()))
    if bfs(c, d) % 2 == 0:
        print("Town")
    else:
        print("Road")