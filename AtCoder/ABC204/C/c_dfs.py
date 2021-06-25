N, M = map(int, input().split())
graph = [0]

for i in range(N):
    graph.append(([]))

for i in range(M):
    A, B = map(int, input().split())
    graph[A].add(B)