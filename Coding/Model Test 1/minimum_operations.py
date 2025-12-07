'''
You are allowed to perform only the following two operations:
1) Add 1
2) Multiply by 2
Your task is to compute, for each target value k in kValues, 
the minimum number of operations required to transform 0 → k using only the above operations.
'''

def count_steps(k):
    steps = 0
    
    while k > 0:
        if k % 2 == 0:
            k //= 2
        else:
            k -= 1
        steps += 1
    return steps

def minimum_operations(kValues):
    return [count_steps(k) for k in kValues]

input_values = [3, 4, 5]
output_values = minimum_operations(input_values)
print(output_values) 