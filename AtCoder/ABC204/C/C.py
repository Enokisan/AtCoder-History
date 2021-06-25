N, M = map(int, input().split())
graph = [0]

for i in range(N):
    graph.append(set([]))

for i in range(M):
    A, B = map(int, input().split())
    graph[A].add(B)

for i in range(N):
    for j in len(graph[i]):
        graph[i].add(graph[graph[i][j]])


print(graph)
