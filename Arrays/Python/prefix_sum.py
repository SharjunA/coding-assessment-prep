def prefix_sum(arr):
    pref = [0] * (len(arr) + 1)
    
    for i, x in enumerate(arr):
        pref[i + 1] = pref[i] + x
    return pref

def range_sum(pref, left, right):
    return pref[right + 1] - pref[left]

input_array = [1, 2, 3, 4, 5]
print(f"Prefix sum of the array {input_array} is: {prefix_sum(input_array)}")
print(f"Sum of elements from index 1 to 3 is: {range_sum(prefix_sum(input_array), 1, 3)}")
