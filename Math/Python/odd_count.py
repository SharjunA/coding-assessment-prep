def odd_count(low, high):
    return (high + 1)//2 - low//2

low = 3
high = 9
print(f"Count of odd numbers between {low} and {high} (inclusive): {odd_count(low, high)}")