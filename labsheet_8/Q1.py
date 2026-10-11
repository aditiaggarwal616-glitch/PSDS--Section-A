n, k = map(int, input().split())
arr = list(map(int, input().split()))
window_sum = sum(arr[:k])
max_sum = window_sum
for i in range(k, n):
    window_sum += arr[i]
    window_sum -= arr[i - k]
    max_sum = max(max_sum, window_sum)
print("Maximum sum:", max_sum)
# 6 3 
# 2 1 5 1 3 2