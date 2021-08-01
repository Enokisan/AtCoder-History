import heapq

Q = int(input())
a = []
heapq.heapify(a)
offset = 0

for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        heapq.heappush(a, query[1]-offset)
    elif query[0] == 2:
        offset += query[1]
    else:
        print(heapq.heappop(a)+offset)
        