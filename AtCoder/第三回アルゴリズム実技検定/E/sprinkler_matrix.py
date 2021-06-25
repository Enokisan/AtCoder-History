N, M, Q = list(map(int, input().split()))

graph = []  #辺があればTrue, なければFalseの隣接行列

for i in range(0, N):
    row = []
    for j in range(0, N):
        row.append(False)
    graph.append(row)

for i in range(0, M):
    u, v = list(map(int, input().split()))

    u -= 1
    v -= 1

    graph[u][v] = True
    graph[v][u] = True

c = list(map(int, input().split()))  # 色についての一次元配列を得る

for i in range(0, Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        x = query[1]

        x -= 1
        print(c[x])

        for i in range(0, N):
            if graph[x][i]:
                c[i] = c[x]
    
    if query[0] == 2:
        x = query[1]
        y = query[2]

        x -= 1
        print(c[x])
        c[x] = y
