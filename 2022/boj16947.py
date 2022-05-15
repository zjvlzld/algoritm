import sys

n=int(sys.stdin.readline())

ans=[-1 for _ in range(n+1)]
route=[[] for _ in range(n+1)]

for _ in range(n):
    a,b=map(int, sys.stdin.readline().split(" "))
    route[a].append(b)
    route[b].append(a)
def cicle(now,stack):
    t=stack[:]
    t.append(now)
    for i in route[now]:
        if i in t and i !=t[-2]:
            for j in range(len(t)-1,-1,-1):
                if(j==i):
                    ans[i]=0
                    return
                ans[t[j]]=0
        if not (i in t):
            cicle(i,t)
    return


def dfs(now,stack):
    t=stack[:]
    if(ans[now]!=-1):
        for i in range(1,len(stack)):
            ans[stack[i]]=len(stack)-i+ans[now]
        return
    t.append(now)
    for i in route[now]:
        if(i !=stack[-1]):
            dfs(i,t)
    
cicle(1,[-1])
for i in range(1,n+1):
    if(len(route[i])==1):
        dfs(i,[-1])

for i in range(1,n+1):
    print(ans[i],end=" ")



# import sys
# from collections import defaultdict, deque

# sys.setrecursionlimit(111111)

# N = int(sys.stdin.readline().strip())
# graph = defaultdict(list)
# answer = [0] * (N + 1)
# visit = [0] * (N + 1)
# traced = []
# cycle = []


# def bfs():
#     dist = [-1] * (N + 1)
#     for i in cycle:
#         dist[i] = 0
#     q = deque(cycle)
#     while q:
#         curr = q.popleft()
#         for next_node in graph[curr]:
#             if dist[next_node] == -1:
#                 dist[next_node] = dist[curr] + 1
#                 q.append(next_node)
#     return dist[1:]


# def dfs(start, curr, cnt):
#     visit[curr] = cnt
#     traced.append(curr) # 방문한 노드를 저장
#     for next_node in graph[curr]:
#         if not visit[next_node]:
#             dfs(start, next_node, cnt + 1)
#         elif next_node in traced:
#             if cnt - visit[next_node] >= 2:
#                 for i in traced[traced.index(next_node):]:
#                     cycle.append(i)
#                 return
#     traced.remove(curr)
#     return


# for _ in range(N):
#     a, b = map(int, sys.stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)

# for node in list(graph):
#     traced = []
#     if not visit[node]:
#         dfs(node, node, 1)

# answer = bfs()
# print(*answer)