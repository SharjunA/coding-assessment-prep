from collections import Counter

def count_repeated_characters(s: str) -> int:
    freq = Counter(s)
    return sum(1 for count in freq.values() if count > 1)

input_string = "programming"
result = count_repeated_characters(input_string)
print(f"Number of distinct characters that appear more than once: {result}")