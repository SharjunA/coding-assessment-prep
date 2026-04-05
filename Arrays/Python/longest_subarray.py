n = int(input())
arr = list(map(int, input().split()))
k = int(input())

prefix_sum = 0
max_len = 0
seen = {0: -1}

for i in range(n):
    prefix_sum += arr[i]

    if prefix_sum - k in seen:
        max_len = max(max_len, i - seen[prefix_sum - k])

    if prefix_sum not in seen:
        seen[prefix_sum] = i

print(max_len)