def longest_zero_subarray(arr):
    prefix_sum_indices = {0: -1}  # Maps prefix sum to its earliest index
    prefix_sum = 0
    max_length = 0
    
    for i, num in enumerate(arr):
        prefix_sum += num
        
        if prefix_sum in prefix_sum_indices:
            max_length = max(max_length, i - prefix_sum_indices[prefix_sum])
        else:
            prefix_sum_indices[prefix_sum] = i
            
    return max_length

input_array = [1, -1, 3, 2, -2, -3, 3]
result = longest_zero_subarray(input_array)
print(result)