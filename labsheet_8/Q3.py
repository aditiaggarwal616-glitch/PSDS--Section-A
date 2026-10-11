N, M, K = map(int, input("Enter N, M and K: ").split())
edges = []
for i in range(M):
    u, v, weight = map(int, input("Enter u, v and weight: ").split())
    edges.append((u, v, weight))
INF = float('inf')
dp = [INF] * (N + 1)
dp[1] = 0
for step in range(K):
    new_dp = dp.copy()
    for u, v, weight in edges:
        if dp[u] != INF:
            new_dp[v] = min(new_dp[v], dp[u] + weight)
        if dp[v] != INF:
            new_dp[u] = min(new_dp[u], dp[v] + weight)

    dp = new_dp
if dp[N] == INF:
    print(-1)
else:
    print("Minimum path weight:", dp[N])