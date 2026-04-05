def run_length_encoding(s):
    if not s:
        return ""
    encoded = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            encoded.append(f"{count}{s[i-1]}")
            count = 1
    
    encoded.append(f"{count}{s[-1]}")
    return ''.join(encoded)

input_string = "aaabbbccdaa"
print(f"Run-length encoding of '{input_string}' is '{run_length_encoding(input_string)}'")

'''
Output: '3a3b2c1d2a'
'''