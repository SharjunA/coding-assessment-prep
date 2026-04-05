s = input()

freq = {}

# Count frequency
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

# Find first non-repeating
for ch in s:
    if freq[ch] == 1:
        print(ch)
        break