N, M = map(int, input().split())
graph = [0]

def search(grap, i):
    r = 0
    if type(grap[i]) is list: 
        for j in grap[i]:
            search(grap, j)
            r += 1
    return r

for i in range(N):
    graph.append([])

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
r = 0
for i in range(N):
    if i == 0:
        continue
    r += search(graph, i)

print(r)