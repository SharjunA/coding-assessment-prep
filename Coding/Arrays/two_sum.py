def two_sum_sorted(arr, target):
    l, r = 0, len(arr) - 1
    
    while l < r:
        two_sum = arr[l] + arr[r]
        
        if two_sum == target:
            return (l, r)
        elif two_sum < target:
            l += 1
        else:   
            r -= 1
    return None


def two_sum(arr, target):
    visited = {}
    
    for i, num in enumerate(arr):
        need = target - num
        
        if need in visited:
            return (visited[need], i)
        visited[num] = i
    return None


def has_pair_with_sum_indices(nums, target):
    visited = {}
    
    for i, x in enumerate(nums):
        needed = target - x
        if needed in visited:
            return True, (visited[needed], i)
        # store index if value not already stored (keeps earliest index)
        if x not in visited:
            visited[x] = i
    return False, None


input_array = [2, 7, 11, 15]
target_value = 9
result = two_sum(input_array, target_value)
print(result)