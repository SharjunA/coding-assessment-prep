from collections import Counter

word = input('Enter a word: ')
for char, count in Counter(word).items():
    print(f"{char}: {count}")
    
'''
freq = {}
for char in word:
    freq[char] = freq.get(char, 0) + 1

for char, count in freq.items():
    print(f"{char}: {count}")
'''