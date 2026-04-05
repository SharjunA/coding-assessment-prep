from collections import Counter

def most_frequent_char(s):
    if not s:
        return ''
    return Counter(s).most_common(1)[0][0]

input_string = "Mississippi"
print(f"The most frequent character in '{input_string}' is '{most_frequent_char(input_string)}'")

'''
most_common(1) -> [('i', 4)]
most_common(1)[0] -> ('i', 4)
most_common(1)[0][0] ->  'i'
'''