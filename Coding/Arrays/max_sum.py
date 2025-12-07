def max_sum(arr, k):
    if k > len(arr):
        return sum(arr)
    
    current_sum = sum(arr[:k])
    max_sum_value = current_sum
    
    for i in range(k, len(arr)):
        current_sum = current_sum + arr[i] - arr[i-k]
        max_sum_value = max(max_sum_value, current_sum)
        
    return max_sum_value

input_array = [2, 1, 5, 1, 3, 2]
k = 3 
print(f"Maximum sum of {k} consecutive elements in the array {input_array} is: {max_sum(input_array, k)}")