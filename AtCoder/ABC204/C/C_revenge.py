N, M = map(int, input().split())
graph = [0]
root_list = [0]

for i in range(N):
    graph.append([])
    root_list.append([])

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

for i in range(N):
    if i == 0:
        continue
    root_list[i].append([i, i])
    root_list[i].append([i, j] for j in graph[i])
    for j in graph[i]:
        