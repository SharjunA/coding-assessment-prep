def is_palindrome(s):
    if not s:
        return True
    
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
        
    return True

input_string = "racecar"
print(f"Is the string '{input_string}' a palindrome? {is_palindrome(input_string)}")    