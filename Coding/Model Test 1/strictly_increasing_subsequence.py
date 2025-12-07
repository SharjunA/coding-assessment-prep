MOD = 10**9 + 7

def count_increasing_subseq_len3(arr):
    n = len(arr)
    total = 0
    
    for j in range(n):
        left_smaller = 0
        right_greater = 0

        # count smaller elements before j
        for i in range(j):
            if arr[i] < arr[j]:
                left_smaller += 1

        # count greater elements after j
        for k in range(j+1, n):
            if arr[k] > arr[j]:
                right_greater += 1

        total += left_smaller * right_greater

    return total % MOD 

arr = [2, 2, 3, 4, 1]
result = count_increasing_subseq_len3(arr)
print(result)